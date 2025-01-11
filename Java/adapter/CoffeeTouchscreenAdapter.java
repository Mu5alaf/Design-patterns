public class CoffeeTouchscreenAdapter implements CoffeeMachineInterface {
    OldCoffeeMachine theMachine;
    
    public CoffeeTouchscreenAdapter(OldCoffeeMachine newMachine){
    theMachine = newMachine;
    }
    @Override
    public void chooseFirstSelection(){
        theMachine.selectA();
    }

    @Override
    public void chooseSecondSelection(){
        theMachine.selectB();
    }

}