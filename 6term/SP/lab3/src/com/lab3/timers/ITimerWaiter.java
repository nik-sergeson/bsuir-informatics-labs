package com.lab3.timers;


public interface ITimerWaiter {
    void TimerNotifyAction(long sec);
    void TimerStopAction();
    void TimerResetAction();
    void TimerInteraptionAction();
}
