
  class BirdWatcher {
      private final int[] birdsPerDay;

      public BirdWatcher(int[] birdsPerDay) {
          this.birdsPerDay = birdsPerDay.clone();
      }

      public int[] getLastWeek() {
          return this.birdsPerDay;
      }

      public int getToday() {
          if (this.birdsPerDay.length == 0)
            return 0;
          else
            return this.birdsPerDay[birdsPerDay.length - 1];
      }

      public void incrementTodaysCount() {
          this.birdsPerDay[this.birdsPerDay.length - 1] = getToday() + 1;
      }

      public boolean hasDayWithoutBirds() {
          for (int bird:this.birdsPerDay){
            if (bird == 0){
              return true;
            }
          }
          return false;
      }

      public int getCountForFirstDays(int numberOfDays) {
        if (numberOfDays > 7){
          numberOfDays = 7;
        }
        int count = 0;
        for (int i = 0; i < numberOfDays; i++){
          count += this.birdsPerDay[i];
        }
        return count;
      }

      public int getBusyDays() {
          int count = 0;
          for (int bird:this.birdsPerDay){
            if (bird >= 5){
              count += 1;
            }
          }
          return count;
      }
  }
