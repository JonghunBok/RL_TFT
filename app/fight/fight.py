import numpy as np
import copy,os
from utils.draw import draw_chess,make_video,find_name
from utils.view import GUI
from buff.synergy import Synergy
from fight.skill import Skill
import time
class Fight:
    '''
    '''
    def __init__(self,my,opp,cur_round):
        myskill = None
        self.cur_round = cur_round
        # first agent info
        self.myunits = my.fight_units
        self.mynum = my.fight_num
        self.myarr = my.fight_arrange
        self.myitems = my.fight_items
        self.mysyn = my.player_synergy
        self.myinfo = my.fight_infos
        self.myname = my.name
        # second agent info
        self.oppunits = opp.fight_units
        self.oppnum = opp.fight_num
        self.opparr = [(6-oa[0],7-oa[1]) for oa in opp.fight_arrange]
        self.oppitems = opp.fight_items
        self.oppsyn = opp.player_synergy
        self.oppinfo = opp.fight_infos
        self.oppname = opp.name
        hexes1 = np.zeros((7,8,34))
        hexes2 = np.zeros((7,8,34))
        self.start_hexes = self._assign_hexes(hexes1,self.mynum,self.myarr,self.myitems,
            self.mysyn,self.myinfo,self.oppnum,self.opparr,self.oppitems,self.oppsyn,
            self.oppinfo,max=True)
        self.cur_hexes = self._assign_hexes(hexes2,self.mynum,self.myarr,self.myitems,
            self.mysyn,self.myinfo,self.oppnum,self.opparr,self.oppitems,self.oppsyn,
            self.oppinfo,max=False)
        self.mysyns = dict()
        self.oppsyns = dict()
        self.mywait = my.wait_units
        self.oppwait = opp.wait_units
    def _assign_hexes(self,hexes,mynum,myarr,myitems,mysyn,myinfo,
        oppnum,opparr,oppitems,oppsyn,oppinfo,max=True):
        '''
        '''
        if max:
            mana = 1
        else:
            mana = 0
        n = 0
        for ou,on,oa,oitem,oinf in zip(self.oppunits,oppnum,opparr,oppitems,oppinfo):
            n += 1
            hexes[oa[0],oa[1],-1] = n
            hexes[oa[0],oa[1],0] = -1
            hexes[oa[0],oa[1],1] = on
            print(find_name(on),oinf['mana'][mana],mana)
            hexes[oa[0],oa[1],2] = oinf['health']
            hexes[oa[0],oa[1],3] = oinf['mana'][mana]
            hexes[oa[0],oa[1],4] = oinf['attack_range']
            hexes[oa[0],oa[1],5] = oinf['attack_damage']
            hexes[oa[0],oa[1],6] = oinf['attack_speed']
            hexes[oa[0],oa[1],7] = oinf['armor']
            hexes[oa[0],oa[1],8] = oinf['magical_resistance']
            # index 9 is is_skill
            # index 10 is sklll damage - config
            hexes[oa[0],oa[1],11] = 0.5
            hexes[oa[0],oa[1],12] = oinf['dodge']
            hexes[oa[0],oa[1],13] = oinf['critical']
            hexes[oa[0],oa[1],14] = oinf['synergy'][0]
            hexes[oa[0],oa[1],15] = oinf['synergy'][1]
            if len(oinf['synergy']) == 3:
                hexes[oa[0],oa[1],16] = oinf['synergy'][2]
            else:
                hexes[oa[0],oa[1],16] = -1
            hexes[oa[0],oa[1],17] = int(ou[-1])
            # index 18 is stunned time
            for c,o in enumerate(oitem):
                hexes[oa[0],oa[1],19+c] = o
            # index 25 is skill shield
            # index 26 is shield remain time
            # index 26 is skill own buff
            # index 27 is skill remain time
        for mu,mn,ma,mitem,minf in zip(self.myunits,mynum,myarr,myitems,myinfo):
            n += 1
            hexes[ma[0],ma[1],-1] = n
            hexes[ma[0],ma[1],0] = 1
            hexes[ma[0],ma[1],1] = mn
            print(find_name(mn),minf['mana'][mana],mana)
            hexes[ma[0],ma[1],2] = minf['health']
            hexes[ma[0],ma[1],3] = minf['mana'][mana]
            hexes[ma[0],ma[1],4] = minf['attack_range']
            hexes[ma[0],ma[1],5] = minf['attack_damage']
            hexes[ma[0],ma[1],6] = minf['attack_speed']
            hexes[ma[0],ma[1],7] = minf['armor']
            hexes[ma[0],ma[1],8] = minf['magical_resistance']
            # index 9 is is_skill
            # index 10 is sklll damage - config
            hexes[ma[0],ma[1],11] = 0.5 # critical damagepercent
            hexes[ma[0],ma[1],12] = minf['dodge']
            hexes[ma[0],ma[1],13] = minf['critical'] # critical prob
            hexes[ma[0],ma[1],14] = minf['synergy'][0]
            hexes[ma[0],ma[1],15] = minf['synergy'][1]
            if len(minf['synergy']) == 3:
                hexes[ma[0],ma[1],16] = minf['synergy'][2]
            else:
                hexes[ma[0],ma[1],16] = -1
            hexes[ma[0],ma[1],17] = int(mu[-1]) # level
            # index 18 is stunned time
            for c,m in enumerate(mitem):
                hexes[ma[0],ma[1],19+c] = m
            # index 25 is skill shield
            # index 26 is shield remain time
            # index 26 is skill own buff
            # index 27 is skill remain time
        return hexes
    def _read_hexes(self,hexes):
        status = hexes[:,:,0]
        oppxy = np.where(status==-1)
        myxy = np.where(status==1)
        self.opparr = [(x,y) for x,y in zip(oppxy[0],oppxy[1])]
        self.myarr = [(x,y) for x,y in zip(myxy[0],myxy[1])]
    def _move(self,hexes,arr1,targ):
        '''
        1 tic에 1 move 가져감.
        todo : 지능적 움직임
        '''
        moved = copy.copy(arr1)
        diff = targ - arr1
        absdiff = abs(diff)
        ind = np.argmax(absdiff)
        if diff[ind] < 0:
            moved[ind] -= 1
            if hexes[moved[0],moved[1],0] != 0:

                moved[ind] += 1
        elif diff[ind] == 0:
            print('error!',targ,arr1)
        else:
            moved[ind] += 1
            if hexes[moved[0],moved[1],0] != 0:
                moved[ind] -= 1
        return moved
    def _fly_infil(self,hexes,arr,you):
        if you == 1:
            find = 7
            signal = -1
        else:
            find = 0
            signal = 1
        while hexes[find,arr[1],0] != 0:
            if find == arr[0]:
                break
            find += signal
        hexes[find,arr[1],:] = hexes[arr[0],arr[1],:]
        hexes[arr[0],arr[1],:] = 0
        return hexes
    def _one_champ_tic(self,hexes,attack_range,arr,you,opp,enemies,tic,
        void=False,sniper=False,pirate=False,starguard=False,protector=False,
        valkyrie=False,infiltrator=False):
        tiles = np.tile(np.array(arr),(len(enemies),1))
        dist = np.max(abs(tiles-enemies),axis=1)
        nearest_dist = np.min(dist)
        ind = np.argmin(dist)
        arrind = hexes[arr[0],arr[1],1]
        if hexes[arr[0],arr[1],18] > 0:
            return hexes,[arrind,'stunned',hexes[arr[0],arr[1],18],arrind]
        elif (tic == 0) and infiltrator:
            print('fly!')
            hexes = self._fly_infil(self,hexes,arr,you)
            attack_info = [arrind,'jump to',arr,arrind]
            return hexes,attack_info
        elif hexes[arr[0],arr[1],9] == 1:
            #print('{} cast skill!'.format(find_name(int(hexes[arr[0],arr[1],1]))))
            self.skill.arr = arr
            hexes,torf = self.skill.cast(opp)
            if torf:
                self._one_champ_tic(hexes,attack_range,arr,you,opp,enemies,tic,
                    sniper=sniper,pirate=pirate,void=void,starguard=starguard,
                    protector=protector,valkyrie=valkyrie,infiltrator=infiltrator)
            if starguard:
                if you == 1:
                    self.mysyns['star_skilled'] += 1
                elif you == -1:
                    self.oppsyns['star_skilled'] += 1
            if protector:
                if you == 1:
                    self.mysyns['protector_skillcast'].append([arr[0],arr[1]])
                elif you == -1:
                    self.oppsyns['protector_skillcast'].append([arr[0],arr[1]])
            attack_info = [arrind,'skill',arr,arrind]
            return hexes,attack_info
        elif attack_range >= nearest_dist:
            cprob = [1-hexes[arr[0],arr[1],13],hexes[arr[0],arr[1],13]]
            if hexes[arr[0],arr[1],13] > 1:
                cprob=[0,1]
            critical = np.random.choice([0,1],p=cprob)
            if valkyrie:
                if hexes[enemies[ind][0],enemies[ind][1],2] <= \
                    self.start_hexes[enemies[ind][0],enemies[ind][1],2] * 0.5:
                    critical = 1
            damage = hexes[arr[0],arr[1],5] - hexes[enemies[ind][0],enemies[ind][1],7]
            damage += critical*(hexes[arr[0],arr[1],11]*(hexes[arr[0],arr[1],5]))
            if void:
                damage = hexes[arr[0],arr[1],5]
            if sniper:
                diff = abs(tiles[ind]-enemies[ind])
                damage += hexes[arr[0],arr[1],5]*(sum(diff)-1)
            if damage < 0:
                damage = 0
            dprob = [hexes[enemies[ind][0],enemies[ind][1],12],1-hexes[enemies[ind][0],enemies[ind][1],12]]
            if hexes[enemies[ind][0],enemies[ind][1],12] > 1:
                dprob = [0,1]
            dodge = np.random.choice([0,1],p=dprob)
            damage = damage * dodge
            #print('{} attack! damage : {}, {}'.format(\
            #    find_name(int(hexes[arr[0],arr[1],1])),damage,hexes[enemies[ind][0],enemies[ind][1],2]))
            #print('shield {}'.format(hexes[enemies[ind][0],enemies[ind][1],25]))
            if hexes[enemies[ind][0],enemies[ind][1],25] > 0 :
                hexes[enemies[ind][0],enemies[ind][1],25] -= damage/tic*hexes[arr[0],arr[1],6]
                if hexes[enemies[ind][0],enemies[ind][1],25] < 0:
                    hexes[enemies[ind][0],enemies[ind][1],2] -= -hexes[enemies[ind][0],enemies[ind][1],25]
            else:
                hexes[enemies[ind][0],enemies[ind][1],2] -= damage/tic*hexes[arr[0],arr[1],6]
            hexes = self._mana(hexes,arr,hit=True)
            hexes = self._mana(hexes,enemies[ind],hit=False)
            if hexes[enemies[ind][0],enemies[ind][1],2] == 0:
                hexes[enemies[ind][0],enemies[ind][1],2] = -1.333
            if hexes[enemies[ind][0],enemies[ind][1],2] < 0:
                if pirate:
                    if you == 1:
                        self.mysyns['pirate_kill'] += 1
                    elif you == -1:
                        self.oppsyns['pirate_kill'] += 1
            arrind = hexes[arr[0],arr[1],1]
            eneind = hexes[enemies[ind][0],enemies[ind][1],1]
            attack_info = copy.copy([eneind,damage/tic*hexes[arr[0],arr[1],6],arr,arrind])
            return hexes,attack_info
        else:
            #print('{} move!'.format(find_name(int(hexes[arr[0],arr[1],1]))))
            targ = enemies[ind]
            eneind = copy.copy(hexes[targ[0],targ[1],1])
            attack_info = [eneind,0]
            moved = self._move(hexes,arr,targ)
            if moved != arr:
                hexes[moved[0],moved[1],:] = hexes[arr[0],arr[1],:]
                self.start_hexes[moved[0],moved[1],:] = self.start_hexes[arr[0],arr[1],:]
                self.start_hexes[arr[0],arr[1],:] = 0
                hexes[arr[0],arr[1],:]  = 0
                #hexes[arr[0],arr[1],26] = -tic-1
            arrind = hexes[moved[0],moved[1],1]
            attack_info += [moved,arrind]
            attack_info = copy.copy(attack_info)
            return hexes,attack_info
    def _mana(self,hexes,arr,hit=True):
        '''
        hit : 10 mana
        damaged by opp : 4
        if skill, next tic skill activate
        '''
        cur_mana = hexes[arr[0],arr[1],3]
        tot_mana = self.start_hexes[arr[0],arr[1],3]
        nm = find_name(int(hexes[arr[0],arr[1],1]))
        #print('{} mana refill {}/{}'.format(nm,cur_mana,tot_mana))
        if tot_mana == 0:
            hexes[arr[0],arr[1],9] = 1
            return hexes
        if hit:
            cur_mana += 5 * hexes[arr[0],arr[1],6]
        else:
            cur_mana += 2
        if cur_mana >= tot_mana:
            hexes[arr[0],arr[1],9] = 1
            cur_mana = 0
        hexes[arr[0],arr[1],3] = cur_mana
        return hexes
    def _is_who(self,hexes,arr,synergy):
        if (hexes[arr[0],arr[1],14]==synergy) or (hexes[arr[0],arr[1],15]==synergy)\
            or (hexes[arr[0],arr[1],16]==synergy):
            is_who = True
        else:
            is_who = False
        return is_who
    def _syn_tic(self,hexes,syns,arr):
        torf = [False]*7
        if syns.is_sniper:
            torf[0] = self._is_who(hexes,arr,19)
        elif syns.is_pirate:
            torf[1] = self._is_who(hexes,arr,6)
        elif syns.is_void:
            torf[2] = self._is_who(hexes,arr,9)
        elif syns.is_starguard:
            torf[3] = self._is_who(hexes,arr,7)
        elif syns.is_protector:
            torf[4] = self._is_who(hexes,arr,18)
        elif syns.is_valkyrie:
            torf[5] = self._is_who(hexes,arr,18)
        elif syns.is_infil:
            torf[6] = self._is_who(hexes,arr,14)
        return torf
    def _fight_tic(self,hexes,n,draw=False,view=False,*kwargs):
        '''2 tic = 1 seconds'''
        tic = 2
        attack_infos = []
        self.mysyns['pirate_kill'] = 0
        self.mysyns['star_skilled'] = 0
        self.mysyns['valkyrie_target'] = []
        self.mysyns['protector_skillcast'] = []
        self.oppsyns['pirate_kill'] = 0
        self.oppsyns['star_skilled'] = 0
        self.oppsyns['valkyrie_target'] = []
        self.oppsyns['protector_skillcast'] = []
        self.skill.tic = n
        tofill = abs(len(self.opparr)-len(self.myarr))
        print('before start',len(self.opparr),len(self.myarr))
        if len(self.opparr) > len(self.myarr):
            self.myarr += [None] * tofill
        else:
            self.opparr += [None] * tofill
        for oa,ma in zip(self.opparr,self.myarr):
            if not (oa == None):
                oa = list(oa)
                oar = hexes[oa[0],oa[1],4]
                mark = hexes[:,:,0]
                oxs,oys = np.where(mark==1)
                oa_enemies = np.array([[x,y] for x,y in zip(oxs,oys)])
                if len(oa_enemies) == 0:
                    pass
                else:
                    osni,opir,ovoi,osta,opro,oval,oinf = self._syn_tic(hexes,self.oppsyn_infos,oa)
                    hexes,attack_info = self._one_champ_tic(hexes,oar,oa,-1,1,oa_enemies,
                        tic,sniper=osni,pirate=opir,void=ovoi,starguard=osta,protector=opro,
                        valkyrie=oval,infiltrator=oinf)
                    attack_infos.append(attack_info)
            print('after oa',len(self.opparr),len(self.myarr))
            if not (ma == None):
                ma = list(ma)
                mar = hexes[ma[0],ma[1],4]
                mark = hexes[:,:,0]
                mxs,mys=np.where(mark==-1)
                ma_enemies = np.array([[x,y] for x,y in zip(mxs,mys)])
                if len(ma_enemies) == 0:
                    pass
                else:
                    msni,mpir,mvoi,msta,mpro,mval,minf = self._syn_tic(hexes,self.mysyn_infos,ma)
                    hexes,attack_info = self._one_champ_tic(hexes,mar,ma,1,-1,ma_enemies,
                        tic,sniper=msni,pirate=mpir,void=mvoi,starguard=msta,protector=mpro,
                        valkyrie=mval,infiltrator=minf)
                    attack_infos.append(attack_info)
            print('after ma',len(self.opparr),len(self.myarr))
        self._read_hexes(hexes)
        if draw:
            self.visualize(hexes,n,attack_infos)
        if view:
            self.accumulate()
        return hexes
    def _off_skill(self):
        self.cur_hexes[:,:,26] -= 1
        on_skill = np.where(self.cur_hexes[:,:,26]==1)
        onx,ony = on_skill
        #print(self.cur_hexes[:,:,26])
        #print(self.cur_hexes[:,:,0])
        #print(self.cur_hexes[:,:,-1])
        for x,y in zip(onx,ony):
            self.skill.arr = [x,y]
            #print('stop!',self.skill.arr)
            self.cur_hexes = self.skill.stop()
    def _off_stun(self):
        self.cur_hexes[:,:,18] -= 1
    def _die(self):
        health = self.cur_hexes[:,:,2]
        dies = np.where(health<0)
        diesx,diesy = dies
        self.mysyns['ds_died'] = 0
        self.oppsyns['ds_died'] = 0
        self.oppsyns['mech_died'] = [False,False]
        self.mysyns['mech_died'] = [False,False]
        for x,y in zip(diesx,diesy):
            who = self.cur_hexes[x,y,0]
            if who == -1:
                if (self.cur_hexes[x,y,14] == 3) or (self.cur_hexes[x,y,15] == 3):
                    self.oppsyns['ds_died'] += 1
                if self.cur_hexes[x,y,1] == 100:
                    self.oppsyns['mech_died'] = [True,[x,y]]
                self.opparr.remove((x,y))
            elif who == 1:
                if (self.cur_hexes[x,y,14] == 3) or (self.cur_hexes[x,y,15] == 3):
                    self.mysyns['ds_died'] += 1
                if self.cur_hexes[x,y,1] == 100:
                    self.mysyns['mech_died'] = [True,[x,y]]
                self.myarr.remove((x,y))
            self.cur_hexes[x,y,:] = 0
    def _end(self):
        '''
        judge the round end & calcul the life change
        '''
        myopp = self.cur_hexes[:,:,0]
        round_damage = [0,3,4,5,10,15,20]
        if self.myarr == []:
            count = len(self.opparr)
            round = round_damage[int(self.cur_round[0])]
            return False,False,count+round
        elif self.opparr == []:
            count = len(self.myarr)
            round = round_damage[int(self.cur_round[0])]
            return False,True,count+round
        else:
            return True,None,0
    def _synergy(self,infos,syns,n):
        infos.tic = n
        infos.ds_died = syns['ds_died']
        infos.mech_died = syns['mech_died']
        infos.pirate_kill = syns['pirate_kill']
        infos.star_skilled = syns['star_skilled']
        infos.valkyrie_target = syns['valkyrie_target']
        infos.protector_skillcast = syns['protector_skillcast']
        infos.tic = n
        infos.hexes = self.cur_hexes
        infos.apply()
        self.cur_hexes = infos.hexes
    def fight(self,video=False):
        notend = True
        n = 0
        self.mysyn_infos = Synergy(self.cur_hexes,self.start_hexes,self.mysyn,n,self.myarr,
            self.opparr)
        self.mysyn_infos.apply()
        self.cur_hexes = self.mysyn_infos.hexes
        self.oppsyn_infos = Synergy(self.cur_hexes,self.start_hexes,self.mysyn,n,self.opparr,
            self.myarr)
        self.oppsyn_infos.apply()
        self.cur_hexes = self.oppsyn_infos.hexes
        #copy_hexes = copy.copy(self.oppsyn_infos.start_hexes)
        #self.start_hexes = copy_hexes
        self.money = 0
        self.item = []
        self.init_view()
        self.skill = Skill(self.cur_hexes,self.start_hexes,tic=n)
        self.skill.mywait = self.mywait
        self.skill.oppwait = self.oppwait
        while notend:
            self._off_skill()
            self._off_stun()
            if n != 0:
                self._synergy(self.mysyn_infos,self.mysyns,n)
                self._synergy(self.oppsyn_infos,self.oppsyns,n)
            self.cur_hexes = self._fight_tic(self.cur_hexes,n,draw=False,view=True)
            self._die()
            self.skill.hexes = self.cur_hexes
            self.skill.maxhexes = self.start_hexes
            notend,win,life_change = self._end()
            n += 1
            if n > 1000:
                self.cur_hexes[:,:,2] = 0
        print('my pirate money {}'.format(self.mysyn_infos.pirate_money))
        print('my pirate money {}'.format(self.mysyn_infos.pirate_item))
        print('enemy pirate money {}'.format(self.oppsyn_infos.pirate_money))
        print('enemy pirate money {}'.format(self.oppsyn_infos.pirate_item))
        if video:
            dir = './fig/{}'.format(self.cur_round)
            make_video(dir,dir+'/{}.avi'.format(self.cur_round))
        return win,life_change
    def visualize(self,hexes,n,attack_infos):
        if not os.path.exists('./fig/{}'.format('ROUND_'+self.cur_round)):
            os.mkdir('./fig/{}'.format('ROUND_'+self.cur_round))
        if not os.path.exists('./fig/{}/{}vs{}'.format('ROUND_'+self.cur_round,self.myname,self.oppname)):
            os.mkdir('./fig/{}/{}vs{}'.format('ROUND_'+self.cur_round,self.myname,self.oppname))
        fn = (4 - len(str(n)))*'0' + str(n)
        imgname = './fig/{}/{}vs{}/frame_{}.jpg'.format('ROUND_'+self.cur_round,self.myname,self.oppname,fn)
        draw_chess(hexes,self.start_hexes,imgname,attack_infos)
    def init_view(self):
        name = []
        cost = []
        is_exist = []
        for champ,c in zip(self.my_queue,self.my_cost):
            if champ:
                name.append(champ)
                cost.append(c)
                is_exist.append(True)
            else:
                name += [None]
                cost += [None]
                is_exist.append(False)
        infos = self.infos()
        self.gui = GUI(60,70,cost,name,is_exist,infos,self.my_money,self.opp_money,
            title='{} vs {}'.format(self.myname,self.oppname),place_table=self.place_table)
    def accumulate(self):
        infos = self.infos()
        self.gui.infos = infos
        self.gui.update_champs(self.gui.game,infos)
        self.gui.root.update()
        time.sleep(0.01)
    def view(self):
        sefl.gui.root.mainloop()
    def infos(self):
        infos = dict()
        n = 0
        self._read_hexes(self.cur_hexes)
        for my in self.myarr:
            ind = self.cur_hexes[my[0],my[1],1]
            heal = int(self.cur_hexes[my[0],my[1],2])
            mana = int(self.cur_hexes[my[0],my[1],3])
            champ = find_name(int(ind))
            infos[my] = [champ,1,self.cur_hexes[my[0],my[1],-1],heal,mana]
            n+=1
        for opp in self.opparr:
            ind = self.cur_hexes[opp[0],opp[1],1]
            heal = int(self.cur_hexes[opp[0],opp[1],2])
            mana = int(self.cur_hexes[opp[0],opp[1],3])
            champ = find_name(int(ind))
            infos[opp] = [champ,-1,self.cur_hexes[opp[0],opp[1],-1],heal,mana]
            n+=1
        return infos
