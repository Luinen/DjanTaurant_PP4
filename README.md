# DJANTAURANT
  

**Welcome to [DJANTAURANT](https://battleshipomega.herokuapp.com/)!**
  

Djantaurant is Dublin's most trusted family-friendly restaurant, where the guest feels like a guest, which is like home. The goals of this  project is to give a user the ability to book appointments, update or cancel. The Target audiance is 

![responsive_pic](/assets/images/battleship_omega.png)

## Features

I explain the website features below.

### **Existing features**
  

- **Tutorial**
  - The tutorial understands the game well for the users.
  - If the users knows the rules, they can skip this part by answering no.
  - Any other response will ask the question again.

  ![tutorial](/assets/images/tutorial_battleship.png)
 

- **Grid**
  - The users can decide the board size. There are 2 options. 5x5 or 10x10.

![board](/assets/images/grid_battleship.png)

- **Placing the ships**
  - After the grid selection, the users can decide where they want to place their ships.
  - The users don't see the the computer choices.
  - The AI randomly generates ships on the board.

- **Target system**
  - Everything is ready to play. The users start and then select the first target and after that the AI does the same.

![target_system](/assets/images/target_battleship.png)

- **End game**
  - The game ends if the user or the computer lose all of their ships.

![game_over](/assets/images/game_over_battleship.png)

### **Features left to implement**
- 2nd board for a longer gameplay
- Multiplayer mode

## Testing

  - I tried to test as many thing as possible on my phone. 
  - I checked all the answers in the tutorial. 


#### **Validator Testing**

- **PYTHON**

  - No errors were returned.
  ![python_checker](/assets/images/python_checker.png)

## Bugs
- Solved Bugs
  - The AI chose the same location and started the game with only 3 or 4 ships.
  - It was possible if the user fired the same spot in the previous rounds.
  - The user was able to use numbers in the tutorial and caused an error. 
  - Fixed an index error, when the users want to put a ship, but it is out of the board range. 
- Unsolved Bugs
  - Unfortunately, I used Heroku and deployed my project, but I couldn't type anything on that site after that. I tried incognito mode, firefox and chrome, but nothing changed. It freezes all the time. I spent 2,5 hours with tutor assistance, they tried many things, but they didn't find the solution.  I also want to thank you from here. It works on other computers.
  - If the users enter nothing when they want to shoot, an error message pop up.

## Deployment  

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  1. In the GitHub repository, navigate to the Settings tab.
  2. From the source section drop-down menu, select the Master Branch.
  3. Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.
  4. The heroku live link can be found here: https://battleshipomega.herokuapp.com/

- If you want to clone the repository:
  1. In the GitHub repository, click on the 'Code'.
  2. Click 'Open with GitHub Desktop' to clone and open the repository with GitHub Desktop.
  3. Click 'Choose...' and, using the Finder window, navigate to a local path where you want to clone the repository. 
  4. Click Clone.  


## Credits

#### Content

- Pirate slangs were taken from [Islads](https://www.islands.com/40-useful-pirate-phrases-for-national-talk-like-pirate-day/).
