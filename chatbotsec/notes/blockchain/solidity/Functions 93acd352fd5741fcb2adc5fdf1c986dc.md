# Functions

A function is a group of reusable code which can be called anywhere in your program.

```solidity
function func_name(parameter-list) scope returns() {
   //statements
}
```

```solidity
pragma solidity ^0.5.0;

contract Test {
   function getResult() public view returns(uint){
      uint a = 1; // local variable
      uint b = 2;
      uint result = a + b;
      return result;
   } 
}
```

# **Function Modifiers**

Function Modifiers are used to modify the behaviour of a function. For example to add a prerequisite to a function.

```solidity
contract Owner {
   modifier onlyOwner {
      require(msg.sender == owner);
      _;
   }
   modifier costs(uint price) {
      if (msg.value >= price) {
         _;
      }
   }
}
```

The function body is inserted where the special symbol " `_;` " appears in the definition of a modifier. So if condition of modifier is satisfied while calling this function, the function is executed and otherwise, an exception is thrown.

```solidity
pragma solidity ^0.5.0;

contract Owner {
   address owner;
   constructor() public {
      owner = msg.sender;
   }
   modifier onlyOwner {
      require(msg.sender == owner);
      _;
   }
   modifier costs(uint price) {
      if (msg.value >= price) {
         _;
      }
   }
}
contract Register is Owner {
   mapping (address => bool) registeredAddresses;
   uint price;
   constructor(uint initialPrice) public { price = initialPrice; }
   
   function register() public payable costs(price) {
      registeredAddresses[msg.sender] = true;
   }
   function changePrice(uint _price) public onlyOwner {
      price = _price;
   }
}
```