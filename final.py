class Player10:
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
		alpha = -100000
		beta = 100000
		return self.ab(temp_board[:],temp_block[:] ,3 , alpha , beta, True,old_move,flag)
	
	def ab(self,board ,block ,depth , alpha , beta,maximize,old_move,flag):
		if(depth == 0):
			#print flag
			return self.heuristic(board,block,flag)

		if maximize:
			utility = -100000
			cells = get_empty_out_of(board,self.blocks_allowed(old_move,block),block);
			for i in cells:
				temp_block = ['-']*9
				for j  in range(0,len(block)):
					temp_block[j] = block[j]

				temp_board = []
				for j in range(9):
					row = ['-']*9
					temp_board.append(row)
				for j in range(0,9):
					for k in range(0,9):
						temp_board[j][k] = board[j][k]
				
				update_lists(temp_board,temp_block,i,flag)
				u_temp = self.ab(temp_board,temp_block,depth - 1, alpha , beta , False,i,flag)				
				#print u_temp, i, depth, old_move , 0 , a , b
				if(u_temp > utility):
					utility = u_temp
					temp = i
				alpha = max(alpha,utility)
				if(beta <= alpha):
					#print u_temp, temp_block, i, depth, 0
					break

			if(depth == 3):
				return temp
			else:
				return utility
		else:
			utility = 100000
			cells = get_empty_out_of(board,self.blocks_allowed(old_move,block),block);
			for i in cells:
		
				temp_block = ['-']*9
				for j in range(0,9):
					temp_block[j] = block[j]

				temp_board = []
				for j in range(9):
					row = ['-']*9
					temp_board.append(row)
				
				for j in range(0,9):
					for k in range(0,9):
						temp_board[j][k] = board[j][k]
				
				flag1 = ''
				if flag == 'x':
					flag1 = 'o'
				elif flag == 'o':
					flag1 = 'x'
				
				update_lists(temp_board , temp_block , i ,flag1 )
				u_temp = self.ab(temp_board,temp_block,depth - 1, alpha , beta , True,i,flag)
				#print u_temp, i, depth , old_move , alpha, beta  , -1
			
				if(u_temp < utility):
					utility = u_temp
					temp = i

				beta = min(beta,utility)
				#print alpha, beta, old_move
				if(beta <= alpha):
					#print u_temp, temp_block, i, depth, -1
					break
			return utility

	def heuristic(self, board, block, flag):
		cnt1 = 0
		cnt2 = 0
		score = 0

		for i in xrange(0,3):
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10

		cnt1 = 0
		cnt2 = 0

		for i in xrange(3,6):
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10


		cnt1 = 0
		cnt2 = 0

		for i in xrange(6,9):
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10

		cnt1 = 0
		cnt2 = 0

		for i in [0, 3, 6]:
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10


		cnt1 = 0
		cnt2 = 0

		for i in [1, 4, 7]:
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10


		cnt1 = 0
		cnt2 = 0

		for i in [2, 5, 8]:
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10


		cnt1 = 0
		cnt2 = 0

		for i in [0, 4, 8]:
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1
		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10

		cnt1 = 0
		cnt2 = 0

		for i in [2, 4, 6]:
			if block[i] == flag:
				cnt1 += 1
			elif block[i] != '-':
				cnt2 += 1

		if cnt1 == 3:
			return 100
		elif cnt2 == 3:
			return -100
		elif cnt1 == 0 and cnt2 == 1:
			score -= 50
		elif cnt1 == 0 and cnt2 == 2:
			score -= 75
		elif cnt2 == 0 and cnt1 == 1:
			score += 50
		elif cnt2 == 0 and cnt1 == 2:
			score += 75
		elif cnt2 < cnt1:
			score += 25
		elif cnt2 > cnt1:
			score -= 25
		elif cnt2 == cnt1:
			score += 10

		return score

	def blocks_allowed(self,old_move,temp_block):
		blocks_allowed  = []
		for_corner = [0,2,3,5,6,8]

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]

		for i in reversed(blocks_allowed):
			if temp_block[i] != '-':
				blocks_allowed.remove(i)
		return blocks_allowed

