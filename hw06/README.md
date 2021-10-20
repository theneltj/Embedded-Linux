### HOMEWORK 6

## YouTube Video
1. National Instruments

2. Linux real time kernel patch

3. Having both real time and non real time tasks that need to cordinate

4. Driver stacks are stored between RT and non RT tasks 

5. The time in which an external event occurs after the event has happened

6. Takes the time stamp and sleeps and reads again to measure the actual sleep time

7. A system that is running a cyclic test on the same hardware one with RT patch and one without

8. DISPATCH: Time it takes for software to dispatch to hardware. SCHEDULING: The time it takes to schedule an interupt

9. How traditional systems deal with real time events

10. the longest running interupt handler in the system

11. Forces IRQ threads through which wake up the handler threads


## PREEMPT_RT

Look at the plots in this file for one with a load and one without a load

The histogram runs until 500 us

## Other Questions

The RT Kernel has a bounded latency because it is injecting threads to shorten the latency bound

We are using a makefile as a load by continuously making and cleaning