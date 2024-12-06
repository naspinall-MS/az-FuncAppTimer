import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */15 * * * *", arg_name="myTimer1", run_on_startup=False,
              use_monitor=False) 
def timer_trigger1(myTimer1: func.TimerRequest) -> None:
    if myTimer1.past_due:
        logging.info('Timer1 is past due!')

    logging.info('Python timer trigger function executed for Timer1.')

@app.timer_trigger(schedule="0 */5 * * * *", arg_name="myTimer2", run_on_startup=False,
              use_monitor=False) 
def timer_trigger2(myTimer2: func.TimerRequest) -> None:
    
    if myTimer2.past_due:
        logging.info('Timer2 is past due!')

    logging.info('Python timer trigger function executed for Timer2.')