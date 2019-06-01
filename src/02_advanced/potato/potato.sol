//this token contract was created by Simon Schuler (sschuler@chaindrium.com) 
//for the Workshop "Supply-Blockchain management" at NConf 2019

pragma solidity >=0.4.22 <0.6.0;

/**
 * The potato contract acts as tokenized potato that is then processed into vodka
 */
contract potato {

    //the name of this potato
    string name;

    //the current owner/holder of this potato
    address owner;

    //the address of the producer
    address producer;

    //the address of the factory
    address factory;

    //is this vodka?
    bool is_vodka;
    
    //is this a bio potato
    bool is_bio;

    constructor(string memory _name, bool _is_bio) public {
        //store the name
        name = _name;
        //set the producer as the one who deployed this contract
        producer = msg.sender;
        //set the current owner of this potato to producer
        owner = producer;
        //set if this potato is bio
        is_bio = _is_bio;
        //currently this is a potato
        is_vodka = false;
    }

    /**
     * modifiers are something that can be declared for functions, they ensure that
     * the code within the modifier is executed before each function that declares 
     * a modifier 
     *
     * this one ensures that specific functions can only be executed by the current owner of this token
     */
    modifier owner_only() { 
        if (msg.sender == owner) {
            //start function code here
            _;
        } else {
            //revert the transaction otherwise
            revert();
        } 
    }

    /**
     * this one esures that only the producer can execute specific functions
     */
    modifier producer_only() { 
        if (msg.sender == producer) {
            //start function code here
            _;
        } else {
            //revert the transaction otherwise
            revert();
        } 
    }

    /**
     * this one esures that only the factory can execute specific functions
     */
    modifier factory_only() { 
        if (msg.sender == factory) {
            //start function code here
            _;
        } else {
            //revert the transaction otherwise
            revert();
        } 
    }

    /**
     * give this potato/vodka to someone else, only the current owner can do this
     */
    function send(address new_owner) owner_only public {
        owner = new_owner;
    }

    /**
     *  sets the factory who makes vodka, only the producer can do this
     */
    function set_factory(address _factory) producer_only public {
        factory = _factory;
    }

    /**
     * marks that this potato was turned into vodka, only the factory can do this
     */
    function to_vodka() factory_only public {
        is_vodka = true;
    }
    
    /**
     * gives back the current owner of this token
     *
     * "view" functions just display data, there is not change in state on the blockchain (thus view)
     * therefore we don't need a transaction to access this value
     */
    function who_is_owner() public view returns(address) {
        return owner;
    }
    
    /**
     * returns if this potato is vodka 
     */
    function is_potato_vodka() public view returns(bool) {
        return is_vodka;
    }
    
    /**
     * returns if this potato is bio
     */
    function is_bio_potato() public view returns(bool) {
        return is_bio;
    }
 
    /**
     * returns the producer
     */
    function who_is_producer() public view returns(address) {
        return producer;
    }
    
    /**
     * returns the factory
     */
    function who_is_factory() public view returns(address) {
        return factory;
    }
    
    /**
     * returns the name of this potato
     */
    function get_name() public view returns(string memory) {
        return name;
    }
}
