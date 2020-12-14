
user_input = int(input())
for i in range(1,user_input+1):
	if user_input % i ==0:
		print(i, end=" ")
		
		# 나눠지는 수들을 i 라고 하고 end""으로 옆으로 이어 쓰기