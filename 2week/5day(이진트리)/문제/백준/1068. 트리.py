# 문제)https://www.acmicpc.net/problem/1068
# 참조)https://blog.naver.com/PostView.naver?blogId=sjy263942&logNo=222182820487&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView

n = int(input())
_parent = list(map(int, input().split()))
delete = int(input())
Trees = [[] for _ in range(n+1)]
root = -1				# root 노드 위치 초기화
cnt = 0					# 리프 노드 수


def dfs(node):
    global Trees, cnt, delete
    if not Trees[node]:			# 해당 노드의 자식노드가 없는 경우(리프노드)
        cnt += 1			# cnt 1 증가
        return

    for j in range(len(Trees[node])):	# 해당 노드의 자식노드 수 만큼 반복
        if Trees[node][j] == delete:	# 자식노드가 삭제할 노드인 경우
            if len(Trees[node]) == 1:	# 자식노드의 수가 1개인 경우
                cnt += 1		# 부모노드가 리프노드가 되므로 cnt 1 증가
            else:
                continue		# 다음 자식노드로 이동
        else:
            dfs(Trees[node][j])		# 자식노드을 매개변수로 dfs 실행


for i in range(len(_parent)):		# n만큼 실행
    if _parent[i] == -1:		# 부모노드가 없는 경우
        root = i			# 루트 노드 지정
    else:
        Trees[_parent[i]].append(i)	# 부모노드 자리에 자식노드 삽입

if delete == root:			# 삭제할 노드가 루트 노드인 경우
    print(0)
else:
    dfs(root)				# dfs를 루트노드부터 실행
    print(cnt)