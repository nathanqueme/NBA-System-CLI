Please enter the new name: 3
Please enter the credit: HiUTS
Traceback (most recent call last):
  File "/home/Association.py", line 87, in <module>
    association.run()
  File "/home/Association.py", line 60, in run
    option = self.handle_option()
             ^^^^^^^^^^^^^^^^^^^^
  File "/home/Association.py", line 66, in handle_option
    self.teams.run()
  File "/home/Teams.py", line 15, in run
    option = self.handle_option()
             ^^^^^^^^^^^^^^^^^^^^
  File "/home/Teams.py", line 26, in handle_option
    self.manage_team()
  File "/home/Teams.py", line 95, in manage_team
    team.run()
  File "/home/Team.py", line 16, in run
    option = self.handle_option()
             ^^^^^^^^^^^^^^^^^^^^
  File "/home/Team.py", line 25, in handle_option
    self.update_player()
  File "/home/Team.py", line 68, in update_player
    credit = float(input( "Please enter the credit: ").strip())
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: could not convert string to float: 'HiUTS'