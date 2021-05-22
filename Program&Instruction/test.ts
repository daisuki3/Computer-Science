interface Labeled {
    label?: string;
  }
  
  function printObj(obj: Labeled){
   
}

  
  let myObj = {
    size: 10,
    label: 'object of size 10'
  }

  printObj(myObj)

let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;

a = ro
a = ro as number[];

interface Bug{
    [x: number]: number;
    [y: string]: string|number;
}

interface ClockConstructor {
    new (hour: number, minute: number);
  }
  
 const Clock: ClockConstructor = class Clock {

    currentTime: Date;
    constructor(h: number, m: number) {}

  }

  interface Shape {
	color: string;
}

interface Square extends Shape {
	length: number;
}

//ok
let square = {} as Square;
square.color = 'blue'
square.length = 10;