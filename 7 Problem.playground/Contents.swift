//: Playground - noun: a place where people can play

import Cocoa
var str = "Hello, playground"

func isPrime(num : Int) -> Bool {
    for i in 2...num-1{
        if num % i == 0 {
            return false
        }
    }
    return true
}

func stPrime(sayi : Int) {
    var primenumbers : [Int] = [2]
    var i : Int = 3
    while primenumbers.count < sayi {
        
        if isPrime(num: i){
            primenumbers.append(i)
            print(i)
            i += 1
        }else {
            i += 1
        }
    }

    
  
}
stPrime(sayi: 100001)



















