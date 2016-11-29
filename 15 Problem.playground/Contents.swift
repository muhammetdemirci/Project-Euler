//: Playground - noun: a place where people can play
let max  = UInt64.max
import Cocoa




func LatticeGrid(x : Int , y : Int ) -> Int{
    var numofPaths : Int = 1

    
    if y > x {

        var bol : Int = 1

        for i in (x+1)...(x+y){
            numofPaths *= i
            if bol <= y {
                numofPaths = numofPaths / bol
                bol += 1
            }
        }
      
    }else{
       
        var bol : Int = 1
        for i in (y+1)...(x+y){
            numofPaths *= i
            print("\(numofPaths) *= \(i)")
            if bol <= x {
                numofPaths = numofPaths / bol
                print("\(numofPaths) = \(numofPaths) / \(bol)")
                bol += 1
            }
           
        }
        
        
    }
    
    
    return numofPaths
}

LatticeGrid(x: 20, y: 20)
