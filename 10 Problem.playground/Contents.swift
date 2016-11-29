//: Playground - noun: a place where people can play

import Cocoa



var primeArray : [Int] = [2]
func isPrime(num : Int) -> Bool {
    for prime in primeArray{
        if num%prime == 0 {
            return false
        }
    }
    var i : Int = 5
    while i*i < num {
        if num % i == 0 || num % (i + 2) == 0 {
            return false
        }
        i += 6
    }

    primeArray.append(num)
    return true
}
func sumBelowNumber(number : Int) -> Int{
    var sum : Int = 2
    
    var index : Int = 3
    while index < number {
        if (isPrime(num: index)){
            sum += index
        }
        index += 2
    }
    
    return sum
}

print(sumBelowNumber(number : 2000000))


primeArray



