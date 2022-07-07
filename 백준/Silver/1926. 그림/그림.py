import sys

n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# n,m = (6, 5)
# arr = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]];
visit = [[False for col in range(m)] for row in range(n)]
cur = (0, 0)
paint = [];
paint_count = 0;
cur_queue = [];
# print(arr, visit)

for y in range(n):
	for x in range(m):
		cur_queue.append((y, x))
		paint_size = 0;

		while True:
			if len(cur_queue) == 0:
				break;

			# print("큐:",cur_queue);
			current_cur = cur_queue.pop();
			

			if arr[current_cur[0]][current_cur[1]] == 1 and not visit[current_cur[0]][current_cur[1]]:
				paint_size += 1;
				visit[current_cur[0]][current_cur[1]] = True;
				#right
				if current_cur[1] + 1 < m and arr[current_cur[0]][current_cur[1] + 1] == 1 and not visit[current_cur[0]][current_cur[1] + 1]:
					cur_queue.append((current_cur[0], current_cur[1] + 1))
				#bottom
				# print("bottom :", (current_cur[0] + 1, current_cur[1]),arr[current_cur[0] + 1][current_cur[1]],  visit[current_cur[0]+1][current_cur[1]]);
				if current_cur[0] + 1 < n and arr[current_cur[0] + 1][current_cur[1]] == 1 and not visit[current_cur[0]+1][current_cur[1]]:
					cur_queue.append((current_cur[0] + 1, current_cur[1]))
				#top
				if current_cur[0] - 1 >= 0 and arr[current_cur[0] - 1][current_cur[1]] == 1 and not visit[current_cur[0] - 1][current_cur[1]]:
					cur_queue.append((current_cur[0] - 1, current_cur[1]))
				#left
				if current_cur[1] - 1 >= 0 and arr[current_cur[0]][current_cur[1] - 1] == 1 and not visit[current_cur[0]][current_cur[1] - 1]:
					cur_queue.append((current_cur[0], current_cur[1] - 1))

			# print(current_cur, paint_size);
		paint.append(paint_size);
		paint_count += paint_size > 0;

print(paint_count)
print(max(paint))