
public abstract class Candy{
    abstract int sweetnees();

    abstract String name();
}

class GumDrop extends Candy{
    @Override
    int sweetnees(){
        return 10 ;
    }
    @Override
    String name(){
        return "Gum drop";
    }
}
class StartBurst extends Candy{
    @Override
    int sweetnees(){
        return 5 ;
    }
    @Override
    String name(){
        return "Star Burst";
    }
}
