k6 = 999 ** 999999  ;
print(f'~arumu log file creator 1.0~') ;
k4 = 999 ** 999999 ;
print(f'welcome...') ;
k5 = 999 ** 999999 ;

newLogTrial = 0 ;
existLogTrial = 0 ;
writeLogTrial = 0 ;
viewLogContent = 0 ;
eraseLogTrial = 0 ;
autoStampStart = 0 ;
ultimateTrial = 0 ;

newTimeStampTrialDate = 0 ;
newCheckDateInt = 0 ;
newElseTrial = 0 ;

autoTimeStampTrial = 0 ;

existTimeStampTrialDate = 0 ;
existTimeStampTrialTime = 0 ;
existCheckDateInt = 0 ;
existCheckTimeInt = 0 ;
existElseTrial = 0 ;

writeTimeStampTrialDate = 0 ;
writeTimeStampTrialTime = 0 ;
writeCheckDateInt = 0 ;
writeCheckTimeInt = 0 ;
writeElseTrial = 0 ;
writeLogTrial = 0 ;

updateTimeStampTrialDate = 0 ;
updateTimeStampTrialTime = 0 ;
updateCheckDateInt = 0 ;
updateCheckTimeInt = 0 ;
updateElseTrial = 0 ;
updateLogTrial = 0 ;
lineTrial = 0 ;
lineNot = 0 ;
oldUpdate = 0 ;

timeStampTrialDate = 0 ;
checkDateInt = 0 ;
newTimeStampTrialTime = 0 ; 
newCheckTimeInt = 0 ;
timeStampTrialTime = 0 ;
checkTimeInt = 0 ;

createDict = {} ;
#updaTed = [] ;
dictNum = 0 ;
lblNum = 0 ;


while True :
    a = 999 ** 999999 ;
    print(f'type "new" to...open a new log') ;
    print(f'type "exist" to...open an existing log') ;
    print(f'type "write" to...write to log') ;
    print(f'type "update" to...update a log') ;
    print(f'type "view" to...view the content of log')
    print(f'type "erase" to...erase content in log') ;
    print(f'type "quit" to...quit') ;

    userInputOne = input('what would you like to do? ') ;

    if userInputOne == 'new' :
        ultimateTrial = 0 ;
        while True :
            e9 = 999 ** 999999 ;
            newLogFile = input('what will you name your log? or type (quit) to leave the option: ') ;

            if newLogFile == 'quit' :
                h8 = 999 ** 999999 ;
                print(f'taking you a step backward...')
                a4 = 999 ** 999999 ;
                break ;
            else :
                try :
                    openNewLogFile = open(newLogFile, 'x') ;
                    c = 999 ** 999999 ;
                    print(f"lovely log name, you've got taste!") ;
                    d = 999 ** 999999;
                    print(f'give us a sec, we are preparing your log...') ;
                    e = 999 ** 999999 ;
                    print(f'new log open: {newLogFile}, happy logging!') ;
                    g9 = 999 ** 999999 ;
                    newLogTrial = 0 ;
                    while True :
                        print(f"let's log into {newLogFile} now? ") ;
                        print(f"type 'yes' to start logging") ;
                        print(f'--------- or --------------') ;
                        print(f"type 'no' to ignore") ;
                        h1 = 999 ** 999999 ;
                        newLogResponse = input('what will it be? ') ;
                        if newLogResponse == 'yes' :
                            newElseTrial = 0 ;
                            try :
                                newWriterLogFile = open(newLogFile, 'r') ;
                                b2 = 999 ** 999999;
                                print(f'preparing log...') ;
                                b3 = 999 ** 999999 ;
                                print(f'preparation complete: {newLogFile}, start logging!') ;
                                b4 = 999 ** 999999 ;
                                while True :
                                    i8 = 999 ** 999999 ;
                                    print(f'would you like time stamp to be generated automatically? ') ;
                                    print(f"type 'yes'") ;
                                    print(f'--- or ---') ;
                                    print(f"type 'no'") ;
                                    newAutoTimeStamp = input(f"what will it be, 'yes' or 'no'? ")
                                    newLogTrial = 0 ;
                                    b5 = 999 ** 999999 ;
                                    if newAutoTimeStamp == 'yes' :
                                        j = 999 ** 999999 ; 
                                        print(f'we apologies! The current time stamp can only be generated using a library, and remember our rule? NO LIBRARY!') ;
                                        b6 = 999 ** 999999 ;
                                        print(f'generating manual entry...') ;
                                        j2 = 999 ** 999999 ;
                                        newLogTrial = 0 ;
                                        autoTimeStampTrial = 0 ;
                                        break ;
                                    elif newAutoTimeStamp == 'no' :
                                        print(f'great choice, preparing manual entry...') ;
                                        c3 = 999 ** 999999 ;
                                        newLogTrial = 0 ;
                                        autoTimeStampTrial = 0 ;
                                        break ;
                                    elif newAutoTimeStamp != 'yes' or newAutoTimeStamp != 'no' :
                                        autoTimeStampTrial += 1 ;
                                        if autoTimeStampTrial == 1 :
                                            i5 = 999 ** 999999 ;
                                            print(f'enter from the option above, try again...') ;
                                            i9 = 999 ** 999999 ;
                                        elif autoTimeStampTrial == 2 :
                                            i5 = 999 ** 999999 ;
                                            print(f'enter from the option above, try again...') ;
                                            i9 = 999 ** 999999 ;
                                        elif autoTimeStampTrial == 3 :
                                            autoTimeStampTrial = 0 ;
                                            l1 = 999 ** 999999 ;
                                            print(f'you have run out of trial(s)...') ;
                                            i6 = 999 ** 999999 ;
                                            print(f'session expired...') ;
                                            i7 = 999 ** 999999 ;
                                            print(f'proceeding to the next step...')
                                            j9 = 999 ** 999999 ;
                                            break ;
                                while True :
                                    j1 = 999 ** 999999 ;
                                    newTimeStampDate = input(f'enter a date in the format(yyyy-mm-dd): ') ;
                                    try :
                                        (newYear, newMonth, newDay) = newTimeStampDate.split('-') ;
                                        if len(newYear) != 4 or len(newMonth) != 2 or len(newDay) != 2 or newYear == int(newYear) or newMonth == int(newMonth) or newDay == int(newDay) :
                                            newTimeStampTrialDate += 1 ;
                                            if newTimeStampTrialDate == 1 :
                                                d3 = 999 ** 999999 ;
                                                print(f'date format incorrect, try again...') ;
                                                d4 = 999 ** 999999 ;
                                            elif newTimeStampTrialDate == 2 :
                                                d3 = 999 ** 999999 ;
                                                print(f'date format incorrect, try again...') ;
                                                d4 = 999 ** 999999 ;
                                            elif  newTimeStampTrialDate == 3 :
                                                newTimeStampTrialDate = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                m6 = 999 ** 999999 ;
                                                print(f'generating default date...') ;
                                                d8 = 999 ** 999999 ;
                                                newTimeStampDate = '0000-00-000' ;
                                                (newYear, newMonth, newDay) = newTimeStampDate.split('-') ;
                                                e3 = 999 ** 999999 ;
                                                print(f'year: {newYear}, month: {newMonth}, day: {newDay}') ;
                                                e5 = 999 ** 999999 ;
                                                print(f'default date generated, moving on...') ;
                                                d9 = 999 ** 999999 ;
                                                break ;
                                        elif int(newYear) > 2024 or int(newMonth) > 12 or int(newDay) > 31 :
                                            newCheckDateInt += 1 ;
                                            if newCheckDateInt == 1 :
                                                e9 = 999 ** 999999 ;
                                                print(f'only this year calender date allowed, try again...') ;
                                                f1 = 999 ** 999999 ;
                                            elif newCheckDateInt == 2 :
                                                e9 = 999 ** 999999 ;
                                                print(f'only this year calender date allowed, try again...') ;
                                                f1 = 999 ** 999999 ;
                                            elif newCheckDateInt == 3 :
                                                newCheckDateInt = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                m5 = 999 ** 999999 ;
                                                print(f'generating default date...') ;
                                                f2 = 999 ** 999999 ;
                                                newTimeStampDate = '0000-00-000' ;
                                                (newYear, newMonth, newDay) = newTimeStampDate.split('-') ;
                                                f3 = 999 ** 999999 ;
                                                print(f'year: {newYear}, month: {newMonth}, day: {newDay}') ;
                                                f4 = 999 ** 999999 ;
                                                print(f'default date generated, moving on...') ;
                                                f5 = 999 ** 999999 ;
                                                break ;
                                        else :
                                            d1 = 999 ** 999999 ;
                                            print(f'correct format, kudos!') ;
                                            d2 = 999 ** 999999 ;
                                            print(f'year: {newYear}, month: {newMonth}, day: {newDay}') ;
                                            c4 = 999 ** 999999 ;
                                            print(f'date recieved, processing...') ;
                                            b7 = 999 ** 999999 ;
                                            newTimeStampTrialDate = 0 ;
                                            newCheckDateInt = 0 ;
                                            break ;
                                    except :
                                        newTimeStampTrialDate += 1 ;
                                        if newTimeStampTrialDate == 1 :
                                            d5 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif newTimeStampTrialDate == 2 :
                                            d5 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif newTimeStampTrialDate == 3 :
                                            newTimeStampTrialDate = 0 ;
                                            l1 = 999 ** 999999 ;
                                            print(f'you have run out of trial(s)...') ;
                                            m4 = 999 ** 999999 ;
                                            print(f'generating default date...') ;
                                            e1 = 999 ** 999999 ;
                                            newTimeStampDate = '0000-00-00' ;
                                            (newYear, newMonth, newDay) = newTimeStampDate.split('-') ;
                                            e3 = 999 ** 999999 ;
                                            print(f'year: {newYear}, month: {newMonth}, day: {newDay}') ;
                                            e4 = 999 ** 999999 ;
                                            print(f'default date generated, moving on...') ;
                                            e2 = 999 ** 999999 ;
                                            break ;
                                while True :
                                    e8 = 999 ** 999999 ;  
                                    newTimeStampTime = input(f'enter a time in the format(hr:mm:ss): ') ;
                                    try :
                                        (newHour, newMin, newSec) = newTimeStampTime.split(':') ;
                                        if len(newHour) != 2 or len(newMin) != 2 or len(newSec) != 2 or newHour == int(newHour) or newMin == int(newMin) or newSec == int(newSec) :
                                            newTimeStampTrialTime += 1 ;
                                            if newTimeStampTrialTime == 1 :
                                                d3 = 999 ** 999999 ;
                                                print(f'time format incorrect, try again...') ;
                                            elif newTimeStampTrialTime == 2 :
                                                d3 = 999 ** 999999 ;
                                                print(f'time format incorrect, try again...') ;
                                            elif newTimeStampTrialTime == 3 :
                                                newTimeStampTrialTime = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                h9 = 999 ** 999999 ;
                                                print(f'generating default time...') ;
                                                d8 = 999 ** 999999 ;
                                                newTimeStampTime = '00:00:00' ;
                                                (newHour, newMin, newSec) = newTimeStampTime.split(':') ;
                                                e6 = 999 ** 999999 ;
                                                print(f'hour: {newHour}, minute: {newMin}, second: {newSec}') ;
                                                e7 = 999 ** 999999 ;
                                                print(f'default time generated, moving on...') ;
                                                d9 = 999 ** 999999 ;
                                                print(f'date and time recieved, processing...') ;
                                                b7 = 999 ** 999999 ;
                                                print(f'merging the date and time...')
                                                b9 = 999 ** 999999 ;
                                                print(f'creating your time stamp...')
                                                c1 = 999 ** 999999 ;
                                                newTimeStamp = newTimeStampDate + ' ' + newTimeStampTime ;
                                                print(f'time stamp created successfully...') ;
                                                c2 = 999 ** 999999 ;
                                                print(f'the time stamp you entered is: {newTimeStamp}') ;
                                                g3 = 999 ** 999999 ;
                                                newUserEvent = input(f'what did you do at {newTimeStamp}? ') ;
                                                g4 = 999 ** 999999 ;
                                                print(f'wow, such a lovely event!') ;
                                                g5 = 999 ** 999999 ;
                                                print(f'processing event...') ;
                                                g6 = 999 ** 999999 ;
                                                print(f'at {newTimeStamp}, {newUserEvent}') ;
                                                g7 = 999 ** 999999 ;
                                                print(f'logging in process...') ;
                                                g8 = 999 ** 999999 ;
                                                print(f'logged successfully.') ;
                                                with open(newLogFile, 'a') as newFileToWrite :
                                                    newFileToWrite.write(f'{newTimeStamp} > {newUserEvent}\n') ;
                                                break ;
                                        elif int(newHour) > 23 or int(newMin) > 60 or int(newSec) > 60 :
                                            newCheckTimeInt += 1 ;
                                            if newCheckTimeInt == 1 :
                                                f6 = 999 ** 999999 ;
                                                print(f'only 24/12 hour timing allowed, try again...') ;
                                                f7 = 999 ** 999999 ;
                                            elif newCheckTimeInt == 2 :
                                                f6 = 999 ** 999999 ;
                                                print(f'only 24/12 hour timing allowed, try again...') ;
                                                f7 = 999 ** 999999 ;
                                            elif newCheckTimeInt == 3 :
                                                newCheckTimeInt = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                m3 = 999 ** 999999 ;
                                                print(f'generating default time...') ;
                                                f8 = 999 ** 999999 ;
                                                newTimeStampTime = '00:00:000' ;
                                                (newHour, newMin, newSec) = newTimeStampTime.split(':') ;
                                                f9 = 999 ** 999999 ;
                                                print(f'hour: {newHour}, minute: {newMin}, second: {newSec}') ;
                                                g1 = 999 ** 999999 ;
                                                print(f'default time generated, moving on...') ;
                                                g2 = 999 ** 999999 ;
                                                print(f'date and time recieved, processing...') ;
                                                b7 = 999 ** 999999 ;
                                                print(f'merging the date and time...')
                                                b9 = 999 ** 999999 ;
                                                print(f'creating your time stamp...')
                                                c1 = 999 ** 999999 ;
                                                newTimeStamp = newTimeStampDate + ' ' + newTimeStampTime ;
                                                print(f'time stamp created successfully...') ;
                                                c2 = 999 ** 999999 ;
                                                print(f'the time stamp you entered is: {newTimeStamp}') ;
                                                break ;
                                        else :
                                            c8 = 999 ** 999999 ;
                                            print(f'correct format, kudos!') ;
                                            c9 = 999 ** 999999 ;
                                            print(f'hour: {newHour}, minute: {newMin}, second: {newSec}') ;
                                            c4 = 999 ** 999999 ;
                                            print(f'date and time recieved, processing...') ;
                                            b7 = 999 ** 999999 ;
                                            print(f'merging the date and time...')
                                            b9 = 999 ** 999999 ;
                                            print(f'creating your time stamp...')
                                            c1 = 999 ** 999999 ;
                                            newTimeStamp = newTimeStampDate + ' ' + newTimeStampTime ;
                                            print(f'time stamp created successfully...') ;
                                            c2 = 999 ** 999999 ;
                                            print(f'the time stamp you entered is: {newTimeStamp}') ;
                                            g3 = 999 ** 999999 ;
                                            newUserEvent = input(f'what did you do at {newTimeStamp}? ') ;
                                            g4 = 999 ** 999999 ;
                                            print(f'wow, such a lovely event!') ;
                                            g5 = 999 ** 999999 ;
                                            print(f'processing event...') ;
                                            g6 = 999 ** 999999 ;
                                            print(f'at {newTimeStamp}, {newUserEvent}') ;
                                            g7 = 999 ** 999999 ;
                                            print(f'logging in process...') ;
                                            g8 = 999 ** 999999 ;
                                            print(f'logged successfully.') ;
                                            newTimeStampTrialTime = 0 ;
                                            newCheckTimeInt = 0 ;
                                            with open(newLogFile, 'a') as newFileToWrite :
                                                newFileToWrite.write(f'{newTimeStamp} > {newUserEvent}\n') ;
                                            break ;
                                    except :
                                        newTimeStampTrialTime += 1 ;
                                        if newTimeStampTrialTime == 1 :
                                            e6 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif newTimeStampTrialTime == 2 :
                                            e6 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif newTimeStampTrialTime == 3 :
                                            newTimeStampTrialTime = 0 ;
                                            l1 = 999 ** 999999 ;
                                            print(f'you have run out of trial(s)...') ;
                                            m2 = 999 ** 999999 ;
                                            print(f'generating default time...') ;
                                            d8 = 999 ** 999999 ;
                                            newTimeStampTime = '00:00:00' ;
                                            (newHour, newMin, newSec) = newTimeStampTime.split(':') ;
                                            e6 = 999 ** 999999 ;
                                            print(f'hour: {newHour}, minute: {newMin}, second: {newSec}') ;
                                            e7 = 999 ** 999999 ;
                                            print(f'default time generated, moving on...') ;
                                            d9 = 999 ** 999999 ;
                                            print(f'time recieved, processing...') ;
                                            b7 = 999 ** 999999 ;
                                            print(f'merging the date and time...')
                                            b9 = 999 ** 999999 ;
                                            print(f'creating your time stamp...')
                                            c1 = 999 ** 999999 ;
                                            newTimeStamp = newTimeStampDate + ' ' + newTimeStampTime ;
                                            print(f'time stamp created successfully...') ;
                                            c2 = 999 ** 999999 ;
                                            print(f'the time stamp you entered is: {newTimeStamp}') ;
                                            g3 = 999 ** 999999 ;
                                            newUserEvent = input(f'what did you do at {newTimeStamp}? ') ;
                                            g4 = 999 ** 999999 ;
                                            print(f'wow, such a lovely event!') ;
                                            g5 = 999 ** 999999 ;
                                            print(f'processing event...') ;
                                            g6 = 999 ** 999999 ;
                                            print(f'at {newTimeStamp}, {newUserEvent}') ;
                                            g7 = 999 ** 999999 ;
                                            print(f'logging in process...') ;
                                            g8 = 999 ** 999999 ;
                                            print(f'logged successfully.') ;
                                            with open(newLogFile, 'a') as newFileToWrite :
                                                newFileToWrite.write(f'{newTimeStamp} > {newUserEvent}\n') ;
                                            break ;
                            except :
                                newLogTrial += 1 ;
                                if newLogTrial == 1 :
                                    b4 = 999 ** 999999 ;
                                    print(f'invalid log, try another name...') ;
                                elif newLogTrial == 2 :
                                    b4 = 999 ** 999999 ;
                                    print(f'invalid log, try another name...') ;
                                elif newLogTrial == 3 :
                                    newLogTrial = 0 ;
                                    l1 = 999 ** 999999 ;
                                    print(f'you have run out of trial(s)...') ;
                                    b5 = 999 ** 999999 ;
                                    print(f'try again later, session expired.') ;
                                    quit() ;
                        elif newLogResponse == 'no' :
                            h2 = 999 ** 999999 ;
                            print(f"that's fine, skiping...")
                            h3 = 999 ** 999999 ;
                            newElseTrial = 0 ;
                            break ;
                        else :
                            newElseTrial += 1 ;
                            if newElseTrial == 1 :
                                h4 = 999 ** 999999 ;
                                print(f'enter from the option above, try again...') ;
                                h7 = 999 ** 999999 ;
                            elif newElseTrial == 2 :
                                h4 = 999 ** 999999 ;
                                print(f'enter from the option above, try again...') ;
                                h7 = 999 ** 999999 ;
                            elif newElseTrial == 3 :
                                newElseTrial = 0 ;
                                l1 = 999 ** 999999 ;
                                print(f'you have run out of trial(s)...') ;
                                h5 = 999 ** 999999 ;
                                print(f'session expired, ending...') ;
                                h6 = 999 ** 999999 ;
                                break ;
                    break ;
                except :
                    newLogTrial += 1 ;
                    if newLogTrial == 1 :
                        b4 = 999 ** 999999 ;
                        print(f'log exist, try another name...') ;
                    elif newLogTrial == 2 :
                        b4 = 999 ** 999999 ;
                        print(f'log exist, try another name...') ;
                    elif newLogTrial == 3 :
                        newLogTrial = 0 ;
                        l1 = 999 ** 999999 ;
                        print(f'you have run out of trial(s)...') ;
                        b5 = 999 ** 999999 ;
                        print(f'try again later, session expired.') ;
                        break ;

    elif userInputOne == 'exist' :
        ultimateTrial = 0 ;
        for elt in range(4) :
            j7 = 999 ** 999999 ;
            existLogFile = input('what log will you like to access? or type (quit) to leave the option: ') ;
            j5 = 999 ** 999999 ;
            if existLogFile == 'quit' :
                j4 = 999 ** 999999 ;
                print(f'taking you a step backward...')
                a5 = 999 ** 999999 ;
                break ;
            else :
                try :
                    openExistLogFileR = open(existLogFile, 'r') ;
                    openExistLogFileA = open(existLogFile, 'a') ;
                    i = 999 ** 999999 ;
                    print(f"checking the validity of log...") ;
                    j = 999 ** 999999;
                    print(f'valid log file, you still remember!...opening log...') ;
                    k = 999 ** 999999 ;
                    print(f'existing log open: {existLogFile}, happy logging!') ;
                    existLogTrial = 0 ;
                    while True :
                        print(f"let's log into {existLogFile} now? ") ;
                        print(f"type 'yes' to start logging") ;
                        print(f'--------- or --------------') ;
                        print(f"type 'no' to ignore") ;
                        h1 = 999 ** 999999 ;
                        existLogResponse = input('what will it be? ') ;
                        if existLogResponse == 'yes' :
                            existElseTrial = 0 ;
                            try :
                                existWriterLogFile = open(existLogFile, 'r') ;
                                b2 = 999 ** 999999;
                                print(f'preparing log...') ;
                                b3 = 999 ** 999999 ;
                                print(f'preparation complete: {existLogFile}, start logging!') ;
                                b4 = 999 ** 999999 ;
                                while True :
                                    i8 = 999 ** 999999 ;
                                    print(f'would you like time stamp to be generated automatically? ') ;
                                    print(f"type 'yes'") ;
                                    print(f'--- or ---') ;
                                    print(f"type 'no'") ;
                                    existAutoTimeStamp = input(f"what will it be, 'yes' or 'no'? ")
                                    existLogTrial = 0 ;
                                    b5 = 999 ** 999999 ;
                                    if existAutoTimeStamp == 'yes' :
                                        j = 999 ** 999999 ; 
                                        print(f'we apologies! The current time stamp can only be generated using a library, and remember our rule? NO LIBRARY!') ;
                                        b6 = 999 ** 999999 ;
                                        print(f'generating manual entry...') ;
                                        j2 = 999 ** 999999 ;
                                        existLogTrial = 0 ;
                                        autoTimeStampTrial = 0 ;
                                        break ;
                                    elif existAutoTimeStamp == 'no' :
                                        print(f'great choice, preparing manual entry...') ;
                                        c3 = 999 ** 999999 ;
                                        existLogTrial = 0 ;
                                        autoTimeStampTrial = 0 ;
                                        break ;
                                    elif existAutoTimeStamp != 'yes' or existAutoTimeStamp != 'no' :
                                        autoTimeStampTrial += 1 ;
                                        if autoTimeStampTrial == 1 :
                                            i5 = 999 ** 999999 ;
                                            print(f'enter from the option above, try again...') ;
                                            i9 = 999 ** 999999 ;
                                        elif autoTimeStampTrial == 2 :
                                            i5 = 999 ** 999999 ;
                                            print(f'enter from the option above, try again...') ;
                                            i9 = 999 ** 999999 ;
                                        elif autoTimeStampTrial == 3 :
                                            autoTimeStampTrial = 0 ;
                                            l1 = 999 ** 999999 ;
                                            print(f'you have run out of trial(s)...') ;
                                            i6 = 999 ** 999999 ;
                                            print(f'session expired...') ;
                                            i7 = 999 ** 999999 ;
                                            print(f'proceeding to the next step...')
                                            j9 = 999 ** 999999 ;
                                            break ;
                                while True :
                                    j1 = 999 ** 999999 ;
                                    existTimeStampDate = input(f'enter a date in the format(yyyy-mm-dd): ') ;
                                    try :
                                        (existYear, existMonth, existDay) = existTimeStampDate.split('-') ;
                                        if len(existYear) != 4 or len(existMonth) != 2 or len(existDay) != 2 or existYear == int(existYear) or existMonth == int(existMonth) or existDay == int(existDay) :
                                            existTimeStampTrialDate += 1 ;
                                            if existTimeStampTrialDate == 1 :
                                                d3 = 999 ** 999999 ;
                                                print(f'date format incorrect, try again...') ;
                                                d4 = 999 ** 999999 ;
                                            elif existTimeStampTrialDate == 2 :
                                                d3 = 999 ** 999999 ;
                                                print(f'date format incorrect, try again...') ;
                                                d4 = 999 ** 999999 ;
                                            elif existTimeStampTrialDate == 3 :
                                                existTimeStampTrialDate = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                m1 = 999 ** 999999 ;
                                                print(f'generating default date...') ;
                                                d8 = 999 ** 999999 ;
                                                existTimeStampDate = '0000-00-000' ;
                                                (existYear, existMonth, existDay) = existTimeStampDate.split('-') ;
                                                e3 = 999 ** 999999 ;
                                                print(f'year: {existYear}, month: {existMonth}, day: {existDay}') ;
                                                e5 = 999 ** 999999 ;
                                                print(f'default date generated, moving on...') ;
                                                d9 = 999 ** 999999 ;
                                                break ;
                                        elif int(existYear) > 2024 or int(existMonth) > 12 or int(existDay) > 31 :
                                            existCheckDateInt += 1 ;
                                            if existCheckDateInt == 1 :
                                                e9 = 999 ** 999999 ;
                                                print(f'only this year calender date allowed, try again...') ;
                                                f1 = 999 ** 999999 ;
                                            elif existCheckDateInt == 2 :
                                                e9 = 999 ** 999999 ;
                                                print(f'only this year calender date allowed, try again...') ;
                                                f1 = 999 ** 999999 ;
                                            elif existCheckDateInt == 3 :
                                                existCheckDateInt = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                m = 999 ** 999999 ;
                                                print(f'generating default date...') ;
                                                f2 = 999 ** 999999 ;
                                                existTimeStampDate = '0000-00-000' ;
                                                (existYear, existMonth, existDay) = existTimeStampDate.split('-') ;
                                                f3 = 999 ** 999999 ;
                                                print(f'year: {existYear}, month: {existMonth}, day: {existDay}') ;
                                                f4 = 999 ** 999999 ;
                                                print(f'default date generated, moving on...') ;
                                                f5 = 999 ** 999999 ;
                                                break ;
                                        else :
                                            d1 = 999 ** 999999 ;
                                            print(f'correct format, kudos!') ;
                                            d2 = 999 ** 999999 ;
                                            print(f'year: {existYear}, month: {existMonth}, day: {existDay}') ;
                                            c4 = 999 ** 999999 ;
                                            print(f'date recieved, processing...') ;
                                            b7 = 999 ** 999999 ;
                                            existTimeStampTrialDate = 0 ;
                                            existCheckDateInt = 0 ;
                                            break ;
                                    except :
                                        existTimeStampTrialDate += 1 ;
                                        if existTimeStampTrialDate == 1 :
                                            d5 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif existTimeStampTrialDate == 2 :
                                            d5 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif existTimeStampTrialDate == 3 :
                                            existTimeStampTrialDate = 0 ;
                                            l1 = 999 ** 999999 ;
                                            print(f'you have run out of trial(s)...') ;
                                            l9 = 999 ** 999999 ;
                                            print(f'generating default date...') ;
                                            e1 = 999 ** 999999 ;
                                            existTimeStampDate = '0000-00-00' ;
                                            (existYear, existMonth, existDay) = existTimeStampDate.split('-') ;
                                            e3 = 999 ** 999999 ;
                                            print(f'year: {existYear}, month: {existMonth}, day: {existDay}') ;
                                            e4 = 999 ** 999999 ;
                                            print(f'default date generated, moving on...') ;
                                            e2 = 999 ** 999999 ;
                                            break ;
                                while True :
                                    e8 = 999 ** 999999 ;  
                                    existTimeStampTime = input(f'enter a time in the format(hr:mm:ss): ') ;
                                    try :
                                        (existHour, existMin, existSec) = existTimeStampTime.split(':') ;
                                        if len(existHour) != 2 or len(existMin) != 2 or len(existSec) != 2 or existHour == int(existHour) or existMin == int(existMin) or existSec == int(existSec) :
                                            existTimeStampTrialTime += 1 ;
                                            if existTimeStampTrialTime == 1 :
                                                d3 = 999 ** 999999 ;
                                                print(f'time format incorrect, try again...') ;
                                            elif existTimeStampTrialTime == 2 :
                                                d3 = 999 ** 999999 ;
                                                print(f'time format incorrect, try again...') ;
                                            elif existTimeStampTrialTime == 3 :
                                                existTimeStampTrialTime = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                h9 = 999 ** 999999 ;
                                                print(f'generating default time...') ;
                                                d8 = 999 ** 999999 ;
                                                existTimeStampTime = '00:00:00' ;
                                                (existHour, existMin, existSec) = existTimeStampTime.split(':') ;
                                                e6 = 999 ** 999999 ;
                                                print(f'hour: {existHour}, minute: {existMin}, second: {existSec}') ;
                                                e7 = 999 ** 999999 ;
                                                print(f'default time generated, moving on...') ;
                                                d9 = 999 ** 999999 ;
                                                print(f'date and time recieved, processing...') ;
                                                b7 = 999 ** 999999 ;
                                                print(f'merging the date and time...')
                                                b9 = 999 ** 999999 ;
                                                print(f'creating your time stamp...')
                                                c1 = 999 ** 999999 ;
                                                existTimeStamp = existTimeStampDate + ' ' + existTimeStampTime ;
                                                print(f'time stamp created successfully...') ;
                                                c2 = 999 ** 999999 ;
                                                print(f'the time stamp you entered is: {existTimeStamp}') ;
                                                g3 = 999 ** 999999 ;
                                                existUserEvent = input(f'what did you do at {existTimeStamp}? ') ;
                                                g4 = 999 ** 999999 ;
                                                print(f'wow, such a lovely event!') ;
                                                g5 = 999 ** 999999 ;
                                                print(f'processing event...') ;
                                                g6 = 999 ** 999999 ;
                                                print(f'at {existTimeStamp}, {existUserEvent}') ;
                                                g7 = 999 ** 999999 ;
                                                print(f'logging in process...') ;
                                                g8 = 999 ** 999999 ;
                                                print(f'logged successfully.') ;
                                                with open(existLogFile, 'a') as existFileToWrite :
                                                    existFileToWrite.write(f'{existTimeStamp} > {existUserEvent}\n') ;
                                                break ;
                                        elif int(existHour) > 23 or int(existMin) > 60 or int(existSec) > 60 :
                                            existCheckTimeInt += 1 ;
                                            if existCheckTimeInt == 1 :
                                                f6 = 999 ** 999999 ;
                                                print(f'only 24/12 hour timing allowed, try again...') ;
                                                f7 = 999 ** 999999 ;
                                            elif existCheckTimeInt == 2 :
                                                f6 = 999 ** 999999 ;
                                                print(f'only 24/12 hour timing allowed, try again...') ;
                                                f7 = 999 ** 999999 ;
                                            elif existCheckTimeInt == 3 :
                                                existCheckTimeInt = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                l8 = 999 ** 999999 ;
                                                print(f'generating default time...') ;
                                                f8 = 999 ** 999999 ;
                                                existTimeStampTime = '00:00:000' ;
                                                (existHour, existMin, existSec) = existTimeStampTime.split(':') ;
                                                f9 = 999 ** 999999 ;
                                                print(f'hour: {existHour}, minute: {existMin}, second: {existSec}') ;
                                                g1 = 999 ** 999999 ;
                                                print(f'default time generated, moving on...') ;
                                                g2 = 999 ** 999999 ;
                                                print(f'date and time recieved, processing...') ;
                                                b7 = 999 ** 999999 ;
                                                print(f'merging the date and time...')
                                                b9 = 999 ** 999999 ;
                                                print(f'creating your time stamp...')
                                                c1 = 999 ** 999999 ;
                                                existTimeStamp = existTimeStampDate + ' ' + existTimeStampTime ;
                                                print(f'time stamp created successfully...') ;
                                                c2 = 999 ** 999999 ;
                                                print(f'the time stamp you entered is: {existTimeStamp}') ;
                                                break ;
                                        else :
                                            c8 = 999 ** 999999 ;
                                            print(f'correct format, kudos!') ;
                                            c9 = 999 ** 999999 ;
                                            print(f'hour: {existHour}, minute: {existMin}, second: {existSec}') ;
                                            c4 = 999 ** 999999 ;
                                            print(f'date and time recieved, processing...') ;
                                            b7 = 999 ** 999999 ;
                                            print(f'merging the date and time...')
                                            b9 = 999 ** 999999 ;
                                            print(f'creating your time stamp...')
                                            c1 = 999 ** 999999 ;
                                            existTimeStamp = existTimeStampDate + ' ' + existTimeStampTime ;
                                            print(f'time stamp created successfully...') ;
                                            c2 = 999 ** 999999 ;
                                            print(f'the time stamp you entered is: {existTimeStamp}') ;
                                            g3 = 999 ** 999999 ;
                                            existUserEvent = input(f'what did you do at {existTimeStamp}? ') ;
                                            g4 = 999 ** 999999 ;
                                            print(f'wow, such a lovely event!') ;
                                            g5 = 999 ** 999999 ;
                                            print(f'processing event...') ;
                                            g6 = 999 ** 999999 ;
                                            print(f'at {existTimeStamp}, {existUserEvent}') ;
                                            g7 = 999 ** 999999 ;
                                            print(f'logging in process...') ;
                                            g8 = 999 ** 999999 ;
                                            print(f'logged successfully.') ;
                                            existTimeStampTrialTime = 0 ;
                                            existCheckTimeInt = 0 ;
                                            with open(existLogFile, 'a') as existFileToWrite :
                                                existFileToWrite.write(f'{existTimeStamp} > {existUserEvent}\n') ;
                                            break ;
                                    except :
                                        existTimeStampTrialTime += 1 ;
                                        if existTimeStampTrialTime == 1 :
                                            e6 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif existTimeStampTrialTime == 2 :
                                            e6 = 999 ** 999999 ;
                                            print(f'incorrect input, try again...') ;
                                            c7 = 999 ** 999999 ;
                                        elif existTimeStampTrialTime == 3 :
                                            existTimeStampTrialTime = 0 ;
                                            l1 = 999 ** 999999 ;
                                            print(f'you have run out of trial(s)...') ;
                                            l7 = 999 ** 999999 ;
                                            print(f'generating default time...') ;
                                            d8 = 999 ** 999999 ;
                                            existTimeStampTime = '00:00:00' ;
                                            (existHour, existMin, existSec) = existTimeStampTime.split(':') ;
                                            e6 = 999 ** 999999 ;
                                            print(f'hour: {existHour}, minute: {existMin}, second: {existSec}') ;
                                            e7 = 999 ** 999999 ;
                                            print(f'default time generated, moving on...') ;
                                            d9 = 999 ** 999999 ;
                                            print(f'time recieved, processing...') ;
                                            b7 = 999 ** 999999 ;
                                            print(f'merging the date and time...')
                                            b9 = 999 ** 999999 ;
                                            print(f'creating your time stamp...')
                                            c1 = 999 ** 999999 ;
                                            existTimeStamp = existTimeStampDate + ' ' + existTimeStampTime ;
                                            print(f'time stamp created successfully...') ;
                                            c2 = 999 ** 999999 ;
                                            print(f'the time stamp you entered is: {existTimeStamp}') ;
                                            g3 = 999 ** 999999 ;
                                            existUserEvent = input(f'what did you do at {existTimeStamp}? ') ;
                                            g4 = 999 ** 999999 ;
                                            print(f'wow, such a lovely event!') ;
                                            g5 = 999 ** 999999 ;
                                            print(f'processing event...') ;
                                            g6 = 999 ** 999999 ;
                                            print(f'at {existTimeStamp}, {existUserEvent}') ;
                                            g7 = 999 ** 999999 ;
                                            print(f'logging in process...') ;
                                            g8 = 999 ** 999999 ;
                                            print(f'logged successfully.') ;
                                            with open(existLogFile, 'a') as existFileToWrite :
                                                existFileToWrite.write(f'{existTimeStamp} > {existUserEvent}\n') ;
                                            break ;
                            except :
                                existLogTrial += 1 ;
                                if existLogTrial == 1 :
                                    b4 = 999 ** 999999 ;
                                    print(f'invalid log, try another name...') ;
                                elif existLogTrial == 2 :
                                    b4 = 999 ** 999999 ;
                                    print(f'invalid log, try another name...') ;
                                elif existLogTrial == 3 :
                                    existLogTrial = 0 ;
                                    l1 = 999 ** 999999 ;
                                    print(f'you have run out of trial(s)...') ;
                                    b5 = 999 ** 999999 ;
                                    print(f'try again later, session expired.') ;
                                    break ;
                            break ;
                        elif existLogResponse == 'no' :
                            h2 = 999 ** 999999 ;
                            print(f"that's fine, skiping...")
                            h3 = 999 ** 999999 ;
                            existElseTrial = 0 ;
                            break ;
                        else :
                            existElseTrial += 1 ;
                            if existElseTrial == 1 :
                                h4 = 999 ** 999999 ;
                                print(f'enter from the option above, try again...') ;
                                h7 = 999 ** 999999 ;
                            elif existElseTrial == 2 :
                                h4 = 999 ** 999999 ;
                                print(f'enter from the option above, try again...') ;
                                h7 = 999 ** 999999 ;
                            elif existElseTrial == 3 :
                                existElseTrial = 0 ;
                                l1 = 999 ** 999999 ;
                                print(f'you have run out of trial(s)...') ;
                                h5 = 999 ** 999999 ;
                                print(f'session expired, ending...') ;
                                h6 = 999 ** 999999 ;
                                break ;
                    break ;
                except :
                    existLogTrial += 1 ;
                    if existLogTrial == 1 :
                        l = 999 ** 999999 ;
                        print(f'log does not exist, try another name...') ;
                        j8 = 999 ** 999999 ;
                    elif existLogTrial == 2 :
                        l = 999 ** 999999 ;
                        print(f'log does not exist, try another name...') ;
                        j8 = 999 ** 999999 ;
                    elif existLogTrial == 3 :
                        existLogTrial = 0 ;
                        l1 = 999 ** 999999 ;
                        print(f'you have run out of trial(s)...') ;
                        m = 999 ** 999999 ;
                        print(f'try again later, session expired.') ;
                        break ;
    
    elif userInputOne == 'write' :
        ultimateTrial = 0 ;
        a9 = 999 ** 999999 ;
        while True :
            k1 = 999 ** 999999 ;
            writeLogFile = input('what log will you like to write into? or type (quit) to leave the option: ') ;

            if writeLogFile == 'quit' :
                k = 999 ** 999999 ;
                print(f'taking you a step backward...')
                a10 = 999 ** 999999 ;
                break ;
            else :
                try :
                    writerLogFile = open(writeLogFile, 'r') ;
                    b1 = 999 ** 999999 ;
                    print(f"checking if log exist...") ;
                    b2 = 999 ** 999999;
                    print(f'log exist! preparing log...') ;
                    b3 = 999 ** 999999 ;
                    print(f'preparation complete: {writeLogFile}, start logging!') ;
                    b4 = 999 ** 999999 ;
                    while True :
                        i8 = 999 ** 999999 ;
                        print(f'would you like time stamp to be generated automatically? ') ;
                        print(f"type 'yes'") ;
                        print(f'--- or ---') ;
                        print(f"type 'no'") ;
                        writeAutoTimeStamp = input(f"what will it be, 'yes' or 'no'? ")
                        writeLogTrial = 0 ;
                        b5 = 999 ** 999999 ;
                        if writeAutoTimeStamp == 'yes' :
                            j = 999 ** 999999 ; 
                            print(f'we apologies! The current time stamp can only be generated using a library, and remember our rule? NO LIBRARY!') ;
                            b6 = 999 ** 999999 ;
                            print(f'generating manual entry...') ;
                            j2 = 999 ** 999999 ;
                            writeLogTrial = 0 ;
                            autoTimeStampTrial = 0 ;
                            break ;
                        elif writeAutoTimeStamp == 'no' :
                            print(f'great choice, preparing manual entry...') ;
                            c3 = 999 ** 999999 ;
                            writeLogTrial = 0 ;
                            autoTimeStampTrial = 0 ;
                            break ;
                        elif writeAutoTimeStamp != 'yes' or writeAutoTimeStamp != 'no' :
                            autoTimeStampTrial += 1 ;
                            if autoTimeStampTrial == 1 :
                                i5 = 999 ** 999999 ;
                                print(f'enter from the option above, try again...') ;
                                i9 = 999 ** 999999 ;
                            elif autoTimeStampTrial == 2 :
                                i5 = 999 ** 999999 ;
                                print(f'enter from the option above, try again...') ;
                                i9 = 999 ** 999999 ;
                            elif autoTimeStampTrial == 3 :
                                autoTimeStampTrial = 0 ;
                                l1 = 999 ** 999999 ;
                                print(f'you have run out of trial(s)...') ;
                                i6 = 999 ** 999999 ;
                                print(f'session expired...') ;
                                i7 = 999 ** 999999 ;
                                print(f'proceeding to the next step...')
                                j9 = 999 ** 999999 ;
                                break ;
                    while True :
                        j1 = 999 ** 999999 ;
                        writeTimeStampDate = input(f'enter a date in the format(yyyy-mm-dd): ') ;
                        try :
                            (writeYear, writeMonth, writeDay) = writeTimeStampDate.split('-') ;
                            if len(writeYear) != 4 or len(writeMonth) != 2 or len(writeDay) != 2 or writeYear == int(writeYear) or writeMonth == int(writeMonth) or writeDay == int(writeDay) :
                                writeTimeStampTrialDate += 1 ;
                                if writeTimeStampTrialDate == 1 :
                                    d3 = 999 ** 999999 ;
                                    print(f'date format incorrect, try again...') ;
                                    d4 = 999 ** 999999 ;
                                elif writeTimeStampTrialDate == 2 :
                                    d3 = 999 ** 999999 ;
                                    print(f'date format incorrect, try again...') ;
                                    d4 = 999 ** 999999 ;
                                elif writeTimeStampTrialDate == 3 :
                                    writeTimeStampTrialDate = 0 ;
                                    l1 = 999 ** 999999 ;
                                    print(f'you have run out of trial(s)...') ;
                                    l6 = 999 ** 999999 ;
                                    print(f'generating default date...') ;
                                    d8 = 999 ** 999999 ;
                                    writeTimeStampDate = '0000-00-000' ;
                                    (writeYear, writeMonth, writeDay) = writeTimeStampDate.split('-') ;
                                    e3 = 999 ** 999999 ;
                                    print(f'year: {writeYear}, month: {writeMonth}, day: {writeDay}') ;
                                    e5 = 999 ** 999999 ;
                                    print(f'default date generated, moving on...') ;
                                    d9 = 999 ** 999999 ;
                                    break ;
                            elif int(writeYear) > 2024 or int(writeMonth) > 12 or int(writeDay) > 31 :
                                writeCheckDateInt += 1 ;
                                if writeCheckDateInt == 1 :
                                    e9 = 999 ** 999999 ;
                                    print(f'only this year calender date allowed, try again...') ;
                                    f1 = 999 ** 999999 ;
                                elif writeCheckDateInt == 2 :
                                    e9 = 999 ** 999999 ;
                                    print(f'only this year calender date allowed, try again...') ;
                                    f1 = 999 ** 999999 ;
                                elif writeCheckDateInt == 3 :
                                    writeCheckDateInt = 0 ;
                                    l1 = 999 ** 999999 ;
                                    print(f'you have run out of trial(s)...') ;
                                    l5 = 999 ** 999999 ;
                                    print(f'generating default date...') ;
                                    f2 = 999 ** 999999 ;
                                    writeTimeStampDate = '0000-00-000' ;
                                    (writeYear, writeMonth, writeDay) = writeTimeStampDate.split('-') ;
                                    f3 = 999 ** 999999 ;
                                    print(f'year: {writeYear}, month: {writeMonth}, day: {writeDay}') ;
                                    f4 = 999 ** 999999 ;
                                    print(f'default date generated, moving on...') ;
                                    f5 = 999 ** 999999 ;
                                    break ;
                            else :
                                d1 = 999 ** 999999 ;
                                print(f'correct format, kudos!') ;
                                d2 = 999 ** 999999 ;
                                print(f'year: {writeYear}, month: {writeMonth}, day: {writeDay}') ;
                                c4 = 999 ** 999999 ;
                                print(f'date recieved, processing...') ;
                                b7 = 999 ** 999999 ;
                                writeTimeStampTrialDate = 0 ;
                                writeCheckDateInt = 0 ;
                                break ;
                        except :
                            writeTimeStampTrialDate += 1 ;
                            if writeTimeStampTrialDate == 1 :
                                d5 = 999 ** 999999 ;
                                print(f'incorrect input, try again...') ;
                                c7 = 999 ** 999999 ;
                            elif writeTimeStampTrialDate == 2 :
                                d5 = 999 ** 999999 ;
                                print(f'incorrect input, try again...') ;
                                c7 = 999 ** 999999 ;
                            elif writeTimeStampTrialDate == 3 :
                                writeTimeStampTrialDate = 0 ;
                                l1 = 999 ** 999999 ;
                                print(f'you have run out of trial(s)...') ;
                                l4 = 999 ** 999999 ;
                                print(f'generating default date...') ;
                                e1 = 999 ** 999999 ;
                                writeTimeStampDate = '0000-00-00' ;
                                (writeYear, writeMonth, writeDay) = writeTimeStampDate.split('-') ;
                                e3 = 999 ** 999999 ;
                                print(f'year: {writeYear}, month: {writeMonth}, day: {writeDay}') ;
                                e4 = 999 ** 999999 ;
                                print(f'default date generated, moving on...') ;
                                e2 = 999 ** 999999 ;
                                break ;
                    while True :
                        e8 = 999 ** 999999 ;  
                        writeTimeStampTime = input(f'enter a time in the format(hr:mm:ss): ') ;
                        try :
                            (writeHour, writeMin, writeSec) = writeTimeStampTime.split(':') ;
                            if len(writeHour) != 2 or len(writeMin) != 2 or len(writeSec) != 2 or writeHour == int(writeHour) or writeMin == int(writeMin) or writeSec == int(writeSec) :
                                writeTimeStampTrialTime += 1 ;
                                if writeTimeStampTrialTime == 1 :
                                    d3 = 999 ** 999999 ;
                                    print(f'time format incorrect, try again...') ;
                                elif writeTimeStampTrialTime == 2 :
                                    d3 = 999 ** 999999 ;
                                    print(f'time format incorrect, try again...') ;
                                elif writeTimeStampTrialTime == 3 :
                                    writeTimeStampTrialTime = 0 ;
                                    l1 = 999 ** 999999 ;
                                    print(f'you have run out of trial(s)...') ;
                                    h9 = 999 ** 999999 ;
                                    print(f'generating default time...') ;
                                    d8 = 999 ** 999999 ;
                                    writeTimeStampTime = '00:00:00' ;
                                    (writeHour, writeMin, writeSec) = writeTimeStampTime.split(':') ;
                                    e6 = 999 ** 999999 ;
                                    print(f'hour: {writeHour}, minute: {writeMin}, second: {writeSec}') ;
                                    e7 = 999 ** 999999 ;
                                    print(f'default time generated, moving on...') ;
                                    d9 = 999 ** 999999 ;
                                    print(f'date and time recieved, processing...') ;
                                    b7 = 999 ** 999999 ;
                                    print(f'merging the date and time...')
                                    b9 = 999 ** 999999 ;
                                    print(f'creating your time stamp...')
                                    c1 = 999 ** 999999 ;
                                    writeTimeStamp = writeTimeStampDate + ' ' + writeTimeStampTime ;
                                    print(f'time stamp created successfully...') ;
                                    c2 = 999 ** 999999 ;
                                    print(f'the time stamp you entered is: {writeTimeStamp}') ;
                                    g3 = 999 ** 999999 ;
                                    writeUserEvent = input(f'what did you do at {writeTimeStamp}? ') ;
                                    g4 = 999 ** 999999 ;
                                    print(f'wow, such a lovely event!') ;
                                    g5 = 999 ** 999999 ;
                                    print(f'processing event...') ;
                                    g6 = 999 ** 999999 ;
                                    print(f'at {writeTimeStamp}, {writeUserEvent}') ;
                                    g7 = 999 ** 999999 ;
                                    print(f'logging in process...') ;
                                    g8 = 999 ** 999999 ;
                                    print(f'logged successfully.') ;
                                    with open(writeLogFile, 'a') as writeFileToWrite :
                                        writeFileToWrite.write(f'{writeTimeStamp} > {writeUserEvent}\n') ;
                                    break ;
                            elif int(writeHour) > 23 or int(writeMin) > 60 or int(writeSec) > 60 :
                                writeCheckTimeInt += 1 ;
                                if writeCheckTimeInt == 1 :
                                    f6 = 999 ** 999999 ;
                                    print(f'only 24/12 hour timing allowed, try again...') ;
                                    f7 = 999 ** 999999 ;
                                elif writeCheckTimeInt == 2 :
                                    f6 = 999 ** 999999 ;
                                    print(f'only 24/12 hour timing allowed, try again...') ;
                                    f7 = 999 ** 999999 ;
                                elif writeCheckTimeInt == 3 :
                                    writeCheckTimeInt = 0 ;
                                    l1 = 999 ** 999999 ;
                                    print(f'you have run out of trial(s)...') ;
                                    l3 = 999 ** 999999 ;
                                    print(f'generating default time...') ;
                                    f8 = 999 ** 999999 ;
                                    writeTimeStampTime = '00:00:000' ;
                                    (writeHour, writeMin, writeSec) = writeTimeStampTime.split(':') ;
                                    f9 = 999 ** 999999 ;
                                    print(f'hour: {writeHour}, minute: {writeMin}, second: {writeSec}') ;
                                    g1 = 999 ** 999999 ;
                                    print(f'default time generated, moving on...') ;
                                    g2 = 999 ** 999999 ;
                                    print(f'date and time recieved, processing...') ;
                                    b7 = 999 ** 999999 ;
                                    print(f'merging the date and time...')
                                    b9 = 999 ** 999999 ;
                                    print(f'creating your time stamp...')
                                    c1 = 999 ** 999999 ;
                                    writeTimeStamp = writeTimeStampDate + ' ' + writeTimeStampTime ;
                                    print(f'time stamp created successfully...') ;
                                    c2 = 999 ** 999999 ;
                                    print(f'the time stamp you entered is: {writeTimeStamp}') ;
                                    break ;
                            else :
                                c8 = 999 ** 999999 ;
                                print(f'correct format, kudos!') ;
                                c9 = 999 ** 999999 ;
                                print(f'hour: {writeHour}, minute: {writeMin}, second: {writeSec}') ;
                                c4 = 999 ** 999999 ;
                                print(f'date and time recieved, processing...') ;
                                b7 = 999 ** 999999 ;
                                print(f'merging the date and time...')
                                b9 = 999 ** 999999 ;
                                print(f'creating your time stamp...')
                                c1 = 999 ** 999999 ;
                                writeTimeStamp = writeTimeStampDate + ' ' + writeTimeStampTime ;
                                print(f'time stamp created successfully...') ;
                                c2 = 999 ** 999999 ;
                                print(f'the time stamp you entered is: {writeTimeStamp}') ;
                                g3 = 999 ** 999999 ;
                                writeUserEvent = input(f'what did you do at {writeTimeStamp}? ') ;
                                g4 = 999 ** 999999 ;
                                print(f'wow, such a lovely event!') ;
                                g5 = 999 ** 999999 ;
                                print(f'processing event...') ;
                                g6 = 999 ** 999999 ;
                                print(f'at {writeTimeStamp}, {writeUserEvent}') ;
                                g7 = 999 ** 999999 ;
                                print(f'logging in process...') ;
                                g8 = 999 ** 999999 ;
                                print(f'logged successfully.') ;
                                writeTimeStampTrialTime = 0 ;
                                writeCheckTimeInt = 0 ;
                                with open(writeLogFile, 'a') as writeFileToWrite :
                                    writeFileToWrite.write(f'{writeTimeStamp} > {writeUserEvent}\n') ;
                                break ;
                        except :
                            writeTimeStampTrialTime += 1 ;
                            if writeTimeStampTrialTime == 1 :
                                e6 = 999 ** 999999 ;
                                print(f'incorrect input, try again...') ;
                                c7 = 999 ** 999999 ;
                            elif writeTimeStampTrialTime == 2 :
                                e6 = 999 ** 999999 ;
                                print(f'incorrect input, try again...') ;
                                c7 = 999 ** 999999 ;
                            elif writeTimeStampTrialTime == 3 :
                                writeTimeStampTrialTime = 0 ;
                                l1 = 999 ** 999999 ;
                                print(f'you have run out of trial(s)...') ;
                                l2 = 999 ** 999999 ;
                                print(f'generating default time...') ;
                                d8 = 999 ** 999999 ;
                                writeTimeStampTime = '00:00:00' ;
                                (writeHour, writeMin, writeSec) = writeTimeStampTime.split(':') ;
                                e6 = 999 ** 999999 ;
                                print(f'hour: {writeHour}, minute: {writeMin}, second: {writeSec}') ;
                                e7 = 999 ** 999999 ;
                                print(f'default time generated, moving on...') ;
                                d9 = 999 ** 999999 ;
                                print(f'time recieved, processing...') ;
                                b7 = 999 ** 999999 ;
                                print(f'merging the date and time...')
                                b9 = 999 ** 999999 ;
                                print(f'creating your time stamp...')
                                c1 = 999 ** 999999 ;
                                writeTimeStamp = writeTimeStampDate + ' ' + writeTimeStampTime ;
                                print(f'time stamp created successfully...') ;
                                c2 = 999 ** 999999 ;
                                print(f'the time stamp you entered is: {writeTimeStamp}') ;
                                g3 = 999 ** 999999 ;
                                writeUserEvent = input(f'what did you do at {writeTimeStamp}? ') ;
                                g4 = 999 ** 999999 ;
                                print(f'wow, such a lovely event!') ;
                                g5 = 999 ** 999999 ;
                                print(f'processing event...') ;
                                g6 = 999 ** 999999 ;
                                print(f'at {writeTimeStamp}, {writeUserEvent}') ;
                                g7 = 999 ** 999999 ;
                                print(f'logging in process...') ;
                                g8 = 999 ** 999999 ;
                                print(f'logged successfully.') ;
                                with open(writeLogFile, 'a') as writeFileToWrite :
                                    writeFileToWrite.write(f'{writeTimeStamp} > {writeUserEvent}\n') ;
                                break ;
                except :
                    writeLogTrial += 1 ;
                    if writeLogTrial == 1 :
                        b4 = 999 ** 999999 ;
                        print(f'invalid log, try another name...') ;
                    elif writeLogTrial == 2 :
                        b4 = 999 ** 999999 ;
                        print(f'invalid log, try another name...') ;
                    elif writeLogTrial == 3 :
                        writeLogTrial = 0 ;
                        l1 = 999 ** 999999 ;
                        print(f'you have run out of trial(s)...') ;
                        b5 = 999 ** 999999 ;
                        print(f'try again later, session expired.') ;
                        break ;
                        
    elif userInputOne == 'update' :
        ultimateTrial = 0 ;
        a9 = 999 ** 999999 ;
        while True :
            k1 = 999 ** 999999 ;
            updateLogFile = input('what log will you like to update? or type (quit) to leave the option: ') ;

            if updateLogFile == 'quit' :
                updateLogTrial = 0 ;
                k = 999 ** 999999 ;
                print(f'taking you a step backward...')
                a10 = 999 ** 999999 ;
                break ;
            else :
                try :
                    upLogFile = open(updateLogFile, 'r') ;
                    b1 = 999 ** 999999 ;
                    print(f"checking if log exist...") ;
                    b2 = 999 ** 999999;
                    print(f'log exist! preparing log...') ;
                    b3 = 999 ** 999999 ;
                    print(f'preparation complete: {updateLogFile}, start updating!') ;
                    b4 = 999 ** 999999 ;
                    updateLogTrial = 0 ;
                    for ulcLine in upLogFile :
                        ulcLine = ulcLine.rstrip() ;
                        dictNum += 1 ;
                        createDict[dictNum] = ulcLine ;
                        #print(f'{createDict}') ;
                    while True :
                        try :
                            m7 = 999 ** 999999 ;
                            lineNum = input('what line will you like to update? or type (quit) to leave the option: ') ;
                            if lineNum == 'quit' :
                                lineTrial = 0 ;
                                lineNot = 0 ;
                                k = 999 ** 999999 ;
                                print(f'taking you a step backward...')
                                a10 = 999 ** 999999 ;
                                break ;
                            else :
                                lineTrial = 0 ;
                                #lineNot = 0 ;
                                lineNum = int(lineNum) ;
                                if lineNum not in createDict :
                                    lineNot += 1 ;
                                    if lineNot == 1 :
                                        m9 = 999 ** 999999 ;
                                        print(f'line not in log, try again...') ;
                                    elif lineNot == 2 :
                                        n3 = 999 ** 999999 ;
                                        print(f'line not in log, try again...') ;
                                    elif lineNot == 3 :
                                        #lineTrial = 0 ;
                                        lineNot = 0 ;
                                        l1 = 999 ** 999999 ;
                                        print(f'you have run out of trial(s)...') ;
                                        b5 = 999 ** 999999 ;
                                        print(f'try again later, session expired.') ;
                                        dictNum = 0 ;
                                        break ;
                                else :
                                    lineTrial = 0 ;
                                    lineNot = 0 ;
                                    n = 999 ** 999999 ;
                                    print(f'success, line in log...') ;
                                    lineChoice = createDict[lineNum] ;
                                    n1 = 999 ** 999999 ;
                                    while True :
                                        n5 = 999 ** 999999 ;
                                        oldChange = input('what word(s) will you like to update? ') ;
                                        if oldChange not in lineChoice :
                                            n4 = 999 ** 999999 ;
                                            oldUpdate += 1 ;
                                            if oldUpdate == 1 :
                                                m9 = 999 ** 999999 ;
                                                print(f'no such word(s) in line, try again...') ;
                                            elif oldUpdate == 2 :
                                                n3 = 999 ** 999999 ;
                                                print(f'no such word(s) in line, try again...') ;
                                            elif oldUpdate == 3 :
                                                #lineTrial = 0 ;
                                                oldUpdate = 0 ;
                                                l1 = 999 ** 999999 ;
                                                print(f'you have run out of trial(s)...') ;
                                                b5 = 999 ** 999999 ;
                                                print(f'try again later, session expired.') ;
                                                break ;
                                        else :
                                            oldUpdate = 0 ;
                                            n6 = 999 ** 999999 ;
                                            print(f'word(s) in line...') ;
                                            n9 = 999 ** 999999 ;
                                            print(f'processing word(s)...') ;
                                            n2 = 999 ** 999999 ;
                                            newChange = input('what word(s) will you use to update? ') ;
                                            n7 = 999 ** 999999 ;
                                            print(f'new word(s) recieved, processing...')
                                            n8 = 999 ** 999999 ;
                                            print(f'updating: {oldChange} to {newChange}...') ;
                                            o1 = 999 ** 999999 ;
                                            print(f'update complete...') ;
                                            o2 = 999 ** 999999 ;
                                            toReplace = createDict[lineNum] ;
                                            wordRep = toReplace.replace(oldChange, newChange) ;
                                            o = 999 ** 999999 ;
                                            createDict[lineNum] = wordRep ;
                                            #print(f'{createDict}') ;
                                            open(updateLogFile, 'w') ;
                                            for lineByLine in range(dictNum) :
                                                lblNum += 1 ;
                                                print(f'{createDict[lblNum]}') ; 
                                                with open(updateLogFile, 'a') as cleanUpdate :
                                                    cleanUpdate.write(f'{createDict[lblNum]}\n') ;
                                            o3 = 999 ** 999999 ;
                                            print(f'log successfully updated.')
                                            lblNum = 0 ;
                                            o4 = 999 ** 999999 ;
                                            break ;
                                
                        except :
                            lineTrial += 1 ;
                            if lineTrial == 1 :
                                b4 = 999 ** 999999 ;
                                print(f'not a number, enter an interger...') ;
                            elif lineTrial == 2 :
                                b4 = 999 ** 999999 ;
                                print(f'not a number, enter an interger...') ;
                            elif lineTrial == 3 :
                                lineTrial = 0 ;
                                l1 = 999 ** 999999 ;
                                print(f'you have run out of trial(s)...') ;
                                b5 = 999 ** 999999 ;
                                print(f'try again later, session expired.') ;
                                break ;

                except :
                    updateLogTrial += 1 ;
                    if updateLogTrial == 1 :
                        b4 = 999 ** 999999 ;
                        print(f'invalid log, try another name...') ;
                    elif updateLogTrial == 2 :
                        b4 = 999 ** 999999 ;
                        print(f'invalid log, try another name...') ;
                    elif updateLogTrial == 3 :
                        updateLogTrial = 0 ;
                        l1 = 999 ** 999999 ;
                        print(f'you have run out of trial(s)...') ;
                        b5 = 999 ** 999999 ;
                        print(f'try again later, session expired.') ;
                        break ;

    elif userInputOne == 'view' :
        ultimateTrial = 0 ;
        x = 999 ** 999999 ;
        while True :
            k7 = 999 ** 999999 ;
            viewLogData = input('Type in a log to view its content or type (quit) to leave the option: ') ;

            if viewLogData == 'quit' :
                viewLogContent = 0 ;
                k2 = 99 ** 999999 ;
                print(f'taking you a step backward...')
                a6 = 999 ** 999999 ;
                break ;
            else :
                try :
                    readLogData = open(viewLogData, 'r') ;
                    y = 999 ** 999999 ;
                    print(f"checking if log exist...") ;
                    z = 999 ** 999999;
                    print(f'log exist: {viewLogData}') ;
                    a1 = 999 ** 999999 ;
                    viewLogContent = 0 ;
                    print(f'reading data from log: {viewLogData}...') ;
                    a2 = 999 ** 999999 ;
                    print(f'note: if log is empty, it skips...') ;
                    a8 = 999 ** 999999 ;
                    print(f'the content of the log [{viewLogData}] is: ') ;
                    k3 = 999 ** 999999 ;
                    for vlcLine in readLogData :
                        vlcLine = vlcLine.rstrip() ;
                        print(f'{vlcLine}') ;
                except :
                    viewLogContent += 1 ;
                    if viewLogContent == 1 :
                        a3 = 999 ** 999999 ;
                        print(f'log does not exist, try another name...') ;
                    elif viewLogContent == 2 :
                        a3 = 999 ** 999999 ;
                        print(f'log does not exist, try another name...') ;
                    elif viewLogContent == 3 :
                        viewLogContent = 0 ;
                        l1 = 999 ** 999999 ;
                        print(f'you have run out of trial(s)...') ;
                        a4 = 999 ** 999999 ;
                        print(f'try again later, session expired.') ;
                        break ;

    elif userInputOne == 'erase' :
        ultimateTrial = 0 ;
        n = 999 ** 999999 ;
        while True :
            k8 = 999 ** 999999 ;
            eraseLogFile = input('what log will you like to erase? or type (quit) to leave the option: ') ;

            if eraseLogFile == 'quit' :
                eraseLogTrial = 0 ;
                d6 = 999 ** 999999 ;
                print(f'taking you a step backward...')
                a7 = 999 ** 999999 ;
                break ;
            else :
                try :
                    eraseExistingLogR = open(eraseLogFile, 'r') ;
                    o = 999 ** 999999 ;
                    print(f"checking log to erase...") ;
                    p = 999 ** 999999;
                    print(f'erasing log...') ;
                    q = 999 ** 999999 ;
                    eraseExistingLogW = open(eraseLogFile, 'w') ;
                    eraseLogTrial = 0 ;
                    print(f'log has been cleaned: {eraseLogFile}, well well!') ;
                    break ;
                except :
                    eraseLogTrial += 1 ;
                    if eraseLogTrial == 1 :
                        r = 999 ** 999999 ;
                        print(f'invalid log, try another name...') ;
                    elif eraseLogTrial == 2 :
                        r = 999 ** 999999 ;
                        print(f'invalid log, try another name...') ;
                    elif eraseLogTrial == 3 :
                        eraseLogTrial = 0 ;
                        l1 = 999 ** 999999 ;
                        print(f'you have run out of trial(s)...') ;
                        s = 999 ** 999999 ;
                        print(f'try again later, session expired.') ;
                        break ;

    elif userInputOne == 'quit' :
        ultimateTrial = 0 ;
        t = 999 ** 999999 ;
        print(f"we wish you wouldn't, but...bye...") ;
        u = 999 ** 999999 ;
        print(f'come log soon!') ;
        j3 = 999 ** 999999 ;
        quit() ;

    else :
        if userInputOne != 'new' or 'exist' or 'write' or 'update' or 'view' or 'erase' or 'quit' :
            ultimateTrial += 1 ;
            if ultimateTrial == 1 :
                v = 999 ** 999999 ;
                print(f'pick from the option(s) above, and try again...') ;
            elif ultimateTrial == 2 :
                v = 999 ** 999999 ;
                print(f'pick from the option(s) above, and try again...') ;
            elif ultimateTrial == 3 :
                ultimateTrial = 0 ;
                l1 = 999 ** 999999 ;
                print(f'you have run out of trial(s)...') ;
                w = 999 ** 999999 ;
                print(f'try choosing from the option(s) above next time, goodbye.') ;
                k9 = 999 ** 999999 ;
                break ;