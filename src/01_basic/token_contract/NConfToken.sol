//this token contract was created by Simon Schuler (sschuler@chaindrium.com) 
//for the Workshop "Supply-Blockchain management" at NConf 2019

pragma solidity >=0.4.22 <0.6.0;

/**
 * The NConfToken contract 
 */
contract NConfToken {

    //the name of this token
    string name;

    //the current owner of this token
    address owner;

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
     * constructor for this token
     */
    constructor(string memory _name) public {
        //the current owner is the one who deployed this token
        owner = msg.sender;
        //store the given name
        name = _name;
    }

    /**
     * transfers this token to the new_owner
     *
     * we use the modifier owner_only to ensure that only the current_owner can send this token to someone else
     *
     * what effectively happens is that the new_owner is stored as current_owner, that's it
     */
    function give(address new_owner) owner_only public {
        owner = new_owner;
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
     * gives back the name of this token
     *
     * "view" functions just display data, there is not change in state on the blockchain (thus view)
     * therefore we don't need a transaction to access this value
     */
    function get_name() public view returns(string memory) {
        return name;
    }
}
