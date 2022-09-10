class queue:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.left = 0
        self.right = -1
        pass

    def enqueue( self , value ) :
        self.arr.insert( self.left , value)
        self.right += 1
        pass

    def dequeue( self ) :
        self.arr.pop( self.right )
        self.right -= 1
        pass

    def showleft( self ) :
        print( self.arr[self.left] )
        pass

    def showright( self ) :
        print( self.arr[self.right] )
        pass

arr=[]
q = queue(arr)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.dequeue()
q.enqueue(1003)
q.showleft()
q.showright()
print(arr)