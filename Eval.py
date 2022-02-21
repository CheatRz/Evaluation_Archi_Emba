
import datetime, time


class Task:
    
	def __init__(self, NAME, PERIOD, COOLDOWN, EXECUTION_TIME, OILNEEDED, PRIORITY = 0, MATERIALCREATED = 0) :
		self.NAME = NAME
		self.PERIOD = PERIOD
		self.COOLDOWN = 0
		self.EXECUTION_TIME = EXECUTION_TIME
		self.OILNEEDED = OILNEEDED
		self.PRIORITY = PRIORITY
		self.MATERIALCREATED = MATERIALCREATED

	
		self.NEXT_DEADLINE = datetime.datetime.now()	

	def run(self):

		global timer
		global tank
		global motors_number
		global wheels_number
		global completed
	
		print(str(timer) + "\t=> " + self.NAME + " started.")
		time.sleep(self.EXECUTION_TIME)
		if self.NAME == 'Pump_1' or self.NAME == 'Pump_2':
			tank = tank + self.MATERIALCREATED
		if self.NAME == 'Machine_1':
			motors_number = motors_number + self.MATERIALCREATED
		if self.NAME == 'Machine_2':
			wheels_number = wheels_number + self.MATERIALCREATED

		tank = tank - self.OILNEEDED
		print(str(timer) + "\t=> " + self.NAME + " finished.")
		self.COOLDOWN = self.PERIOD
					
		if wheels_number >= 4 and motors_number >= 1:
			wheels_number = 0
			motors_number = 0
			completed = completed + 1
			

if __name__ == "__main__":

	# Definition of all tasks and instanciation
	task_list  = [
		Task(NAME = 'PUMP_1', PERIOD = 5, COOLDOWN = 0, EXECUTION_TIME = 2, PRIORITY = 3, MATERIALCREATED = 10, OILNEEDED = 0),
		Task(NAME = 'PUMP_2', PERIOD =  15, COOLDOWN = 0, EXECUTION_TIME = 3, PRIORITY = 3, MATERIALCREATED = 20, OILNEEDED = 0),
		Task(NAME = 'MACHINE_1', PERIOD = 5, COOLDOWN = 0, EXECUTION_TIME = 5, PRIORITY = 3, MATERIALCREATED = 1, OILNEEDED = 25),
		Task(NAME = 'MACHINE_2', PERIOD = 5, COOLDOWN = 0, EXECUTION_TIME = 3, PRIORITY = 3, MATERIALCREATED = 1, OILNEEDED = 5) ]

	global timer
	timer = -1

	# Global scheduling loop
	while(True) :
		
		task_to_run = None
		timer += 1
		global tank

		# Choose the task to be run
		for current_task in task_list  :

			if current_task.COOLDOWN > 0 or current_task.OILNEEDED > tank:
				current_task.COOLDOWN = current_task.COOLDOWN - 1
				current_task.PRIORITY = 3
				continue

			if current_task.NAME == 'Pump_1' or current_task.NAME == 'Pump_2':
				if tank + current_task.MATERIALCREATED > 50:
					current_task.PRIORITY = 3
			
			if current_task.NAME == 'MACHINE_1':
				if wheels_number / 4 < motors_number:
					current_task.PRIORITY = 1
				if wheels_number / 4 > motors_number:
					current_task.PRIORITY = 2				
				if motors_number >= 1 :
					current_task.PRIORITY = 3

			if current_task.NAME == 'MACHINE_2':
				if wheels_number / 4 < motors_number:
					current_task.PRIORITY = 2
				if wheels_number / 4 > motors_number:
					current_task.PRIORITY = 1
				if wheels_number >= 1 :
					current_task.PRIORITY = 3





					
		
		if task_to_run == None :
			time.sleep(1)
			print(str(timer) + "\tIdle")
		else :
			task_to_run.run()

