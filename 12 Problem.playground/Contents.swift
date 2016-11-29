//: Playground - noun: a place where people can play

import Cocoa


func find_num_of_divisor(number : Int) -> Int {
    var num_of_divisor : Int = 0
    for i in 1...number{
        if number % i == 0 {
            num_of_divisor += 1
        }
    }
    
    return num_of_divisor
}

func Find_triangle_numbers_as_number_of_divisor(number : Int) -> Int{
    var triangle_num : Int = 0
    var num_of_divisor : Int = 0
    var index : Int = 1
    while num_of_divisor < number{
        triangle_num = triangle_num + index
        index += 1
        num_of_divisor = find_num_of_divisor(number: triangle_num)
    }
    
    return triangle_num
    
}

Find_triangle_numbers_as_number_of_divisor(number: 500)
