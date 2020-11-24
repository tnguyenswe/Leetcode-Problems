

        z=set()
        for i in nums:
            if i in z:
                return True
            else:
                 z.add(i)
        return False
