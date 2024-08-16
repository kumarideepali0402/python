e=Entry(key,value)
        is_present=False
        index=e.hash%self.__cap
        for i in range(len(self.__data[index])):
            if(self.__data[index][i].key==key):
                self.__data[index][i]=e
                is_present=True
                break
            if(not is_present):
                self.__data[index].append(e)
                self.__size+=1