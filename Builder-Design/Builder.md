Builder design pattern is mostly useful in the scenarios where we wanted to have multiple number of parameters.
It is hard to remember each and every parameter provided in the constructor 
The constrcutor becomes overloaded
There will be no flexibility to set only one parameter 
It becomes more complex and tightly coupled with the class and make the application more complex 

### Solution 

We will follow the builder Design Method.
Splitting the object creation process into separable steps.
This method is useful and most effective because it is implemented through "Method Chanining": Means chain the methods in a object to provide the values 

