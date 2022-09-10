class stack:
    def __init__( self, arr ) -> None:
        self.arr= arr
        self.top = -1
        pass
    
    def push( self,value ): 
        self.value = value        
        self.arr.insert( self.top + 1 , value )
        self.top += 1 
        pass
    
    def pop( self ):
        self.arr.pop( self.top )
        self.top -= 1
        pass
    
    def showtop( self ):
        return self.arr[self.top]
        pass
    
arr = []
st = stack(arr)
st.push(1)
st.push(12)
st.push(14)
st.pop()
st.pop()
st.push(552)
st.push(45)
st.push(11)
st.push(115)
st.push(121)
st.push(111)
st.pop()
top= st.showtop()
print(arr,top)
