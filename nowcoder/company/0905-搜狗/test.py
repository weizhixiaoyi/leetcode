#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param arr float浮点型一维数组
# @return int整型
#
class Solution:
    def find_best_cut(self, arr):
        arr_len = len(arr)
        arr_sum = sum(arr)
        ave_list = []
        cur_sum = 0
        for i in range(arr_len - 1):
            cur_sum += arr[i]
            left_ave = cur_sum / (i + 1)
            right_ave = (arr_sum - cur_sum) / (arr_len - (i + 1))
            ave_list.append([left_ave, right_ave])
        # print(ave_list)

        # left_v
        # left_v = []
        # left_sum = 0
        # for i in range(arr_len - 1):
        #     left_sum += (arr[i] - ave_list[i][0]) ** 2
            # print(arr[i], ave_list[i][0], left_sum)
            # left_v.append(left_sum / (i + 1))
        # print(left_v)

        min_idx = 0
        min_v = float('inf')
        for i in range(arr_len - 1):
            # left
            left_v = 0
            for j in range(i + 1):
                left_v += (arr[j] - ave_list[i][0]) ** 2
            left_v /= (i + 1)

            # right
            right_v = 0
            for j in range(i + 1, arr_len):
                right_v += (arr[j] - ave_list[i][1]) ** 2
            right_v /= (arr_len - (i + 1))

            v = left_v + right_v
            if v < min_v:
                min_v = v
                min_idx = i
            if i > arr_len // 2:
                break
        return min_idx + 1


if __name__ == '__main__':
    arr = [1, 1, 1, 3, 3, 3]
    ans = Solution().find_best_cut(arr)
    print(ans)
