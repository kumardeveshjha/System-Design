 Factory Design Pattern is a Low level Design Pattern which is Particularly used when we frequesntly update the services/feautures to the main interface of the client.

 Without the factory Pattern it leads to break the open-close principle and may make the code more complex 
 The factory pattern.
 
 We have to make changes to the client facing class that makes it more complex and bad practice of programming.

 The client side class is tightly coupled with the specific service class 

###  With Factory Pattern -->

Factory pattern moves all object creation logic into oe central place - the factory class. 

Instead of creating objects directly throughout the code, this responsibility is handled by the factory that handles which specific class to be build according to the request.

This also ensures the open-close principle should be avided.


