var c = parseInt(readline())

for(let i = 0; i < c; i++){
    let tmp = readline()
    unzip(tmp)
                                                  
}      

function unzip(zipped){
    let stack = []

    for(let i = 0; i < zipped.length; i++){
        if(zipped[i] === ")"){

            let index = stack.lastIndexOf("(")

            let str = stack.slice(index + 1).join("")//复制
            stack.splice(index)//元素出栈

            
            let count = ""
            i = i + 1
            for(; i < zipped.length; i++){
                if(isNaN(parseInt(zipped[i])) === false){
                    count = count + zipped[i]
                }
                else{
                    break
                }
            }
            i = i - 1
            count = parseInt(count)

            for(let j = 0; j < count; j++){
                stack = stack.concat(str)
            }

        }
        else if(isNaN(parseInt(zipped[i])) === false){

            let count = zipped[i]
            i = i + 1
            for(; i < zipped.length; i++){
                if(isNaN(parseInt(zipped[i])) === false){
                    count = count + zipped[i]
                }
                else{
                    break
                }
            }
            i = i - 1
            count = parseInt(count)
            count = count - 1
            let last = stack[stack.length - 1]


            for(let j = 0; j < count; j++){
                stack = stack.concat(last)
            }
        }
        else{
            stack.push(zipped[i])
        }
    }

    console.log(stack.join(""))
}

