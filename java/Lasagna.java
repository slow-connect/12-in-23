public class Lasagna {
  private int COOKING_TIME = 40;
  private int PREPARATION_TIME = 2;

    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven() {
      return COOKING_TIME;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int time) {
      return COOKING_TIME - time;
    }
    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layers) {
      return PREPARATION_TIME * layers;
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layers, int time) {
      return preparationTimeInMinutes(layers) + time;
    }
}
