package com.lab3.timers;


public class TimeCounter implements Runnable {
    private long timeleft;
    private long delay;
    private long mintime;
    private long starttime;
    private boolean active;
    private boolean pause;
    private ITimerWaiter timerWaiter;

    public TimeCounter(long starttime,long mintime,ITimerWaiter timerWaiter){
        this.timeleft=starttime;
        this.starttime=starttime;
        this.mintime=mintime;
        delay=1000;
        active=false;
        this.timerWaiter=timerWaiter;
        pause=false;
    }

    public void Reset() {
        timeleft=starttime;
        timerWaiter.TimerResetAction();
    }

    public void Pause(){
        pause=true;
    }

    public void Resume(){
        pause=false;
    }

    public void Stop(){
        active=false;
        timerWaiter.TimerInteraptionAction();
    }

    public void run() {
        active=true;
        while (active) {
            if (timeleft <= 0) {
                active = false;
                timerWaiter.TimerStopAction();
                return;
            }
            if (timeleft < mintime && !pause)
                timerWaiter.TimerNotifyAction(timeleft);
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            if(!pause)
                timeleft -= delay / 1000;
        }
    }

    public boolean isActive() {
        return active;
    }
}
