// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!
// Examples:
// pushFront([5,7,2,3], 8) => [8,5,7,2,3] // [num,5,7,2,3]
// pushFront([99], 7) => [7,99]
// Solution 1: using for loop (shift all values to right {decrement} then add the new value)
function pushFront(arr,num){
    for (i = arr.length; i> 0; i--){
        arr[i] = arr[i-1]
    }
    arr[0] = num
    return arr
}

// Solution 2: using push built in function {using for loop and push each value or use ...}
// function pushFront(arr,num){
//     var arr2 = [num]
//     // arr2.push(arr)
//     // arr.forEach(element => {
//     //     arr2.push(element)
//     // });
//     arr2.push(...arr)
//     return arr2
// }

console.log(pushFront([5,7,2,3], 8))
//-------------------------------------------------------------------------------------------------------
// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!
// Examples:
// popFront([0,5,10,15]) => 0 returned, with [5,10,15] printed in the function
// popFront([4,5,7,9]) => 4 returned, with [5,7,9] printed in the function
// function popFront(arr){
//     num = arr[0]
//     for(i=0; i<arr.length; i++){
//         arr[i] = arr[i+1]
//     }
//     arr.pop()
//     console.log(arr)
//     return num
// }

function popFront(arr){
    num = arr[0]
    for(i=0; i<arr.length-1; i++){
        arr[i] = arr[i+1]
    }
    arr.pop()
    console.log(arr)
    return num
}
console.log(popFront([0,5,10,15]))
//-------------------------------------------------------------------------------------------------------
// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!
// Examples:
// insertAt([100,200,5], 2, 311) => [100,200,311,5]
// insertAt([9,33,7], 1, 42) => [9,42,33,7]
function insertAt(arr,index,value){
    

}