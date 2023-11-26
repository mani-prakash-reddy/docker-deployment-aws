import streamlit as st
import random

options = ["Rock", "Paper", "Scissors"]


def get_computer_choice():
    return random.choice(options)


def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        st.warning("It's a tie!",icon="🤝")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        st.success("You win!",icon="🎉")
        st.balloons()
    elif player_choice == "Paper" and computer_choice == "Rock":
        st.success("You win!", icon="🎉")
        st.balloons()
    elif player_choice == "Scissors" and computer_choice == "Paper":
        st.success("You win!", icon="🎉")
        st.balloons()
    else:
        st.error("You lose!", icon="😢")


st.title("Rock Paper Scissors")

col = st.columns(3)

with col[0]:
	button_rock = st.button("Rock")
with col[1]:
	button_paper = st.button("Paper")
with col[2]:
	button_scissors = st.button("Scissors")


computer_choice = get_computer_choice()


if button_rock:
	player_choice = "Rock"
	st.write(f"You chose {player_choice} and the computer chose {computer_choice}")
	get_winner(player_choice, computer_choice)
	
 
if button_paper:
	
	player_choice = "Paper"
	st.write(f"You chose {player_choice} and the computer chose {computer_choice}")
	get_winner(player_choice, computer_choice)

if button_scissors:
	player_choice = "Scissors"
	st.write(f"You chose {player_choice} and the computer chose {computer_choice}")
	get_winner(player_choice, computer_choice)


