import random
from collections import defaultdict
from tkinter import *

class Main_window(object):
    def __init__(self, master):
        self.game_window=Frame(master)
        self.game_window.grid()

        self.game=Score_frame(self.game_window)
        self.dice=Dice(self.game_window)

class Dice(object):
    dice_var=[0,0,0,0,0]
    save_var=[0,0,0,0,0]
    def __init__(self, master):
        self.play_frame=Frame(master)
        self.play_frame.grid(row=0, column=2)

        self.save_dice()
        self.roll_dice()
        self.buttons()

    def roll_dice(self):
        self.roll_frame=Frame(self.play_frame)
        self.roll_frame.grid(row=1, columnspan=4)

        self.turn_counter=2

        self.dice_var=list()
        for num in range(0,5):
            rand=random.randint(1,6)
            self.dice_var.append(rand)

        Dice.dice_var=self.dice_var

        self.die1_button=Button(self.roll_frame, text=self.dice_var[0], command=self.die1)
        self.die1_button.grid(row=0, column=0)

        self.die2_button=Button(self.roll_frame, text=self.dice_var[1], command=self.die2)
        self.die2_button.grid(row=0, column=1)

        self.die3_button=Button(self.roll_frame, text=self.dice_var[2], command=self.die3)
        self.die3_button.grid(row=0, column=2)

        self.die4_button=Button(self.roll_frame, text=self.dice_var[3], command=self.die4)
        self.die4_button.grid(row=0, column=4)

        self.die5_button=Button(self.roll_frame, text=self.dice_var[4], command=self.die5)
        self.die5_button.grid(row=0, column=5)

    def save_dice(self):
        self.saved=Frame(self.play_frame)
        self.saved.grid(row=0, columnspan=4)

        self.die1_label=Label(self.saved, text=Dice.save_var[0])
        self.die1_label.grid(row=0, column=0)

        self.die2_label=Label(self.saved, text=Dice.save_var[1])
        self.die2_label.grid(row=0, column=1)

        self.die3_label=Label(self.saved, text=Dice.save_var[2])
        self.die3_label.grid(row=0, column=2)

        self.die4_label=Label(self.saved, text=Dice.save_var[3])
        self.die4_label.grid(row=0, column=3)

        self.die5_label=Label(self.saved, text=Dice.save_var[4])
        self.die5_label.grid(row=0, column=4)

    def die1(self):
        Dice.save_var[0]=(self.dice_var[0])
        self.die1_label.configure(text=self.dice_var[0])
        self.die1_button.configure(state= 'disabled', disabledforeground = self.roll_frame.cget('bg'))

    def die2(self):
        Dice.save_var[1]=(self.dice_var[1])
        self.die2_label.configure(text=self.dice_var[1])
        self.die2_button.configure(state= 'disabled', disabledforeground = self.roll_frame.cget('bg'))

    def die3(self):
        Dice.save_var[2]=(self.dice_var[2])
        self.die3_label.configure(text=self.dice_var[2])
        self.die3_button.configure(state= 'disabled', disabledforeground = self.roll_frame.cget('bg'))

    def die4(self):
        Dice.save_var[3]=(self.dice_var[3])
        self.die4_label.configure(text=self.dice_var[3])
        self.die4_button.configure(state= 'disabled', disabledforeground = self.roll_frame.cget('bg'))

    def die5(self):
        Dice.save_var[4]=(self.dice_var[4])
        self.die5_label.configure(text=self.dice_var[4])
        self.die5_button.configure(state= 'disabled', disabledforeground = self.roll_frame.cget('bg'))

    def buttons(self):
        self.button_frame=Frame(self.play_frame)
        self.button_frame.grid(row=2)

        Dice.button_frame=self.button_frame

        self.roll_button=Button(self.button_frame, text='roll', command=self.roll_command)
        self.roll_button.grid(row=0)

        self.next_button=Button(self.button_frame, text='next', command=self.next_command)
        self.next_button.grid(row=0, column=1)

        self.exit_button=Button(self.button_frame, text='exit', command=sys.exit)
        self.exit_button.grid(row=0, column=2)

    def next_command(self):
        Dice.save_var=[0,0,0,0,0]
        self.roll_button.configure(state='active')
        self.roll_dice()
        self.save_dice()
        print(Dice.save_var, self.turn_counter)

    def roll_command(self):
        self.turn_counter-=1
        if self.turn_counter==0:
            self.roll_button['state']='disabled'
            self.dice_var=list()
            for num in range(0,5):
                rand=random.randint(1,6)
                self.dice_var.append(rand)

        else:
            self.dice_var=list()
            for num in range(0,5):
                rand=random.randint(1,6)
                self.dice_var.append(rand)

        Dice.dice_var=self.dice_var

        self.die1_button.configure(text=self.dice_var[0])
        self.die2_button.configure(text=self.dice_var[1])
        self.die3_button.configure(text=self.dice_var[2])
        self.die4_button.configure(text=self.dice_var[3])
        self.die5_button.configure(text=self.dice_var[4])

class Score_frame(object):
    upper_sub_total=0
    lower_total=0

    def __init__(self, master):
        self.score_frame=Frame(master)
        self.score_frame.grid(rowspan=9)

        self.upper=self.upper_section(self.score_frame)
        self.lower=self.lower_section(self.score_frame)

        self.end_game_but=Button(self.score_frame, text='End Game', command=self.end_game_command)
        self.end_game_but.pack()

    def end_game_command(self):
        self.bonus=0
        if Score_frame.upper_sub_total>62:
            self.bonus=35
        self.upper_total=Score_frame.upper_sub_total+self.bonus
        self.upper_total_var['text']=self.upper_total
        self.upper_var['text']=self.upper_total

        self.lower_total_var['text']=Score_frame.lower_total
        self.total_var['text']=self.upper_total+Score_frame.lower_total

    def upper_section(self, upper):
        self.upper_frame=Frame(self.score_frame)
        self.upper_frame.pack()

        self.one_label=Label(self.upper_frame, text="One's")
        self.one_label.grid(row=0)

        self.one_var=Button(self.upper_frame, text='--', command=self.one_but)
        self.one_var.grid(row=0, column=1)

        self.two_label=Label(self.upper_frame, text="Two's")
        self.two_label.grid(row=0, column=2)

        self.two_var=Button(self.upper_frame, text='--', command=self.two_but)
        self.two_var.grid(row=0, column=3)

        self.three_label=Label(self.upper_frame, text="Three's")
        self.three_label.grid(row=1)

        self.three_var=Button(self.upper_frame, text='--', command=self.three_but)
        self.three_var.grid(row=1, column=1)

        self.four_label=Label(self.upper_frame, text="Four's")
        self.four_label.grid(row=1, column=2)

        self.four_var=Button(self.upper_frame, text='--', command=self.four_but)
        self.four_var.grid(row=1, column=3)

        self.five_label=Label(self.upper_frame, text="Five's")
        self.five_label.grid(row=2)

        self.five_var=Button(self.upper_frame, text='--', command=self.five_but)
        self.five_var.grid(row=2, column=1)

        self.six_label=Label(self.upper_frame, text="Six's")
        self.six_label.grid(row=2, column=2)

        self.six_var=Button(self.upper_frame, text='--', command=self.six_but)
        self.six_var.grid(row=2, column=3)

        self.upper_sub_total_label=Label(self.upper_frame, text="Sub Total:")
        self.upper_sub_total_label.grid(row=3)

        self.upper_sub_total_var=Label(self.upper_frame, text='--')
        self.upper_sub_total_var.grid(row=3, column=1)

        self.upper_bonus_label=Label(self.upper_frame, text="Bonus:")
        self.upper_bonus_label.grid(row=3, column=2)

        self.upper_bonus_var=Label(self.upper_frame, text='--')
        self.upper_bonus_var.grid(row=3, column=3)

        self.upper_total_label=Label(self.upper_frame, text="Total:")
        self.upper_total_label.grid(row=4)

        self.upper_total_var=Label(self.upper_frame, text='--')
        self.upper_total_var.grid(row=4, column=1)

    def one_but(self):
        update_value=0
        for num in Dice.save_var:
            if num == 1:
                update_value+=num
        self.one_var.configure(text=update_value, state='disabled')
        Score_frame.upper_sub_total+=update_value
        self.upper_sub_total_var['text']=Score_frame.upper_sub_total

    def two_but(self):
        update_value=0
        for num in Dice.save_var:
            if num == 2:
                update_value+=num
        self.two_var.configure(text=update_value, state='disabled')
        Score_frame.upper_sub_total+=update_value
        self.upper_sub_total_var['text']=Score_frame.upper_sub_total

    def three_but(self):
        update_value=0
        for num in Dice.save_var:
            if num == 3:
                update_value+=num
        self.three_var.configure(text=update_value, state='disabled')
        Score_frame.upper_sub_total+=update_value
        self.upper_sub_total_var['text']=Score_frame.upper_sub_total

    def four_but(self):
        update_value=0
        for num in Dice.save_var:
            if num == 4:
                update_value+=num
        self.four_var.configure(text=update_value, state='disabled')
        Score_frame.upper_sub_total+=update_value
        self.upper_sub_total_var['text']=Score_frame.upper_sub_total

    def five_but(self):
        update_value=0
        for num in Dice.save_var:
            if num == 5:
                update_value+=num
        self.five_var.configure(text=update_value, state='disabled')
        Score_frame.upper_sub_total+=update_value
        self.upper_sub_total_var['text']=Score_frame.upper_sub_total

    def six_but(self):
        update_value=0
        for num in Dice.save_var:
            if num == 6:
                update_value+=num
        self.six_var.configure(text=update_value, state='disabled')
        Score_frame.upper_sub_total+=update_value
        self.upper_sub_total_var['text']=Score_frame.upper_sub_total


    def lower_section(self, lower):
        self.lower_frame=Frame(self.score_frame)
        self.lower_frame.pack()

        self.three_kind_label=Label(self.lower_frame, text="3 of a kind:")
        self.three_kind_label.grid(row=0)

        self.three_kind_var=Button(self.lower_frame, text=0, command=self.three_kind_command)
        self.three_kind_var.grid(row=0, column=1)

        self.four_kind_label=Label(self.lower_frame, text="4 of a kind:")
        self.four_kind_label.grid(row=0, column=2)

        self.four_kind_var=Button(self.lower_frame, text=0, command=self.four_kind_command)
        self.four_kind_var.grid(row=0, column=3)

        self.full_house_label=Label(self.lower_frame, text="full_house:")
        self.full_house_label.grid(row=1)

        self.full_house_var=Button(self.lower_frame, text=0, command=self.full_house_command)
        self.full_house_var.grid(row=1, column=1)

        self.sm_straight_label=Label(self.lower_frame, text="sm_straight:")
        self.sm_straight_label.grid(row=1, column=2)

        self.sm_straight_var=Button(self.lower_frame, text=0, command=self.sm_straight_command)
        self.sm_straight_var.grid(row=1, column=3)

        self.lg_straight_label=Label(self.lower_frame, text="lg_straight:")
        self.lg_straight_label.grid(row=2)

        self.lg_straight_var=Button(self.lower_frame, text=0, command=self.lg_straight_command)
        self.lg_straight_var.grid(row=2, column=1)

        self.yahtzee_label=Label(self.lower_frame, text="YAHTZEE:")
        self.yahtzee_label.grid(row=2, column=2)

        self.yahtzee_var=Button(self.lower_frame, text=0, command=self.yahtzee_command)
        self.yahtzee_var.grid(row=2, column=3)

        self.lower_total_label=Label(self.lower_frame, text="lower total:")
        self.lower_total_label.grid(row=3)

        self.lower_total_var=Label(self.lower_frame, text=0)
        self.lower_total_var.grid(row=3, column=1)

        self.upper_total_label=Label(self.lower_frame, text="upper total:")
        self.upper_total_label.grid(row=3, column=2)

        self.upper_var=Label(self.lower_frame, text=0)
        self.upper_var.grid(row=3, column=3)

        self.total_label=Label(self.lower_frame, text="Grand Total:")
        self.total_label.grid(row=4)

        self.total_var=Label(self.lower_frame, text=0)
        self.total_var.grid(row=4, column=1)

    def three_kind_command(self):
        update_value=0
        d = defaultdict(int)
        print(Dice.save_var)
        for num in Dice.save_var:
            d[num] +=1
        result = max(d.items(), key=lambda x: x[1])
        print(result)
        if result[1]>=3:
            update_value=result[0]*result[1]
        self.three_kind_var.configure(text=update_value, state='disabled')
        Score_frame.lower_total+=update_value

    def four_kind_command(self):
        update_value=0
        d = defaultdict(int)
        print(Dice.save_var)
        for num in Dice.save_var:
            d[num] +=1
        result = max(d.items(), key=lambda x: x[1])
        print(result)
        if result[1]>=4:
            update_value=result[0]*result[1]
        self.four_kind_var.configure(text=update_value, state='disabled')
        Score_frame.lower_total+=update_value

    def full_house_command(self):
        update_value=0
        d = defaultdict(int)
        for num in Dice.save_var:
            d[num] +=1
        if 2 and 3 in list(d.values()):
            update_value=25
        self.full_house_var.configure(text=update_value, state='disabled')
        Score_frame.lower_total+=update_value

    def sm_straight_command(self):
        update_value=0
        pos_sm_straight=[[0,1,2,3,4],[0,2,3,4,5],[0,3,4,5,6]]
        print(sorted(Dice.save_var))
        if sorted(Dice.save_var) in pos_sm_straight:
            update_value=30
        self.sm_straight_var.configure(text=update_value, state='disabled')
        Score_frame.lower_total+=update_value

    def lg_straight_command(self):
        update_value=0
        pos_lg_straight=[[1,2,3,4,5],[2,3,4,5,6]]
        if sorted(Dice.save_var) in pos_lg_straight:
            update_value=40
        self.lg_straight_var.configure(text=update_value, state='disabled')
        Score_frame.lower_total+=update_value

    def yahtzee_command(self):
        update_value=0
        d = defaultdict(int)
        print(Dice.save_var)
        for num in Dice.save_var:
            d[num] +=1
        result = max(d.items(), key=lambda x: x[1])
        print(result)
        if result[1]>=5:
            update_value=50
        self.yahtzee_var.configure(text=update_value, state='disabled')
        Score_frame.lower_total+=update_value


if __name__ in "__main__":
    root= Tk()
    root.title("Yahzee")
    root.geometry=('200x200')
    main_window=Main_window(root)
    root.mainloop()