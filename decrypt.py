 def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]

        if k>0:
            sum_num=sum(code[1:1+k])

            ans.append(sum_num)

            for i in range(1,len(code)):

                sum_num=sum_num-code[i]+code[(i+k)%len(code)]
                ans.append(sum_num)


            return ans


        elif k<0:

            k=-k
            sum_num=sum(code[-k:])
            ans.append(sum_num)

            for i in range(1,len(code)):

                sum_num+=code[i-1]-code[(i-k-1)%len(code)]
                ans.append(sum_num)

            return ans

        else:

            return [0]*len(code)
