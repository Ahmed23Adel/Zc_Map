import { Component } from '@angular/core';
import { SolutionBackedService } from './solution-backed.service';
import { Subject } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  ////////////////////////////////////
  ///////Send signal from App component to Zc map
  /////// If equal to +1, then it will catch a click otherwise it will not
  ////////it will send this signal based on signal coming from search area
  signalCatchFromMain = "-1"//if +1 don't catch mouse, if -1 catch it
  signalCatchToMain = "-1"//if +1 don't catch mouse, if -1 catch it
  ////////////////////////////////////

  ////////////////////////////////////
  ///////value of  x, y that user selected. to be sent to search area.
  ////// it t should  have been set by zc map
  msgSearchAreaFrom = ""
  msgSearchAreaTo = ""
  //////////////////////////////////
  /////////////////////////////////
  ///// tmp var I   store msgSearchAreaFrom, and msgSearchAreaTo before sending  them to 
  ///// search area 
  valueFromParent = "0,0";
  valueToParent = "0,0";
  /////////////////////////////////
  ////// send  final signal to zc-map to search to call API
  eventsSubject: Subject<void> = new Subject<void>();
  ////////////////////////////////////////

  FinalFrom = ""
  FinalTo = ""
  FinalChecked = ""


  title = 'lellyMaps';
  signalFromSearchArea = ""

  ///////////////////////////////////////
  ////// some variables to hold from, to, checked, algorithm
  ///////// it should be set by emiiter in   search area
  FinalFromParent = ""
  FinalToParent = ""
  FinalCheckedParent = ""
  FinalAloParent = ""
  ///////////////////////////////////////
  /////////////////////////////////////
  /////  These are   the variables that are being  read by
  ///// the zc-map that should be set  while calling an API
  FinalFromToZcMap: any;
  FinalToToZcMap: any;
  FinalAlgToZcMap: any;
  FinalCheckedToZcMap: any;

  constructor(private solServiceData:SolutionBackedService){}

  catchFrom(){
    /*
    This func is fired by search area component, 
    when it does, it sets the value of signalCatchFrom to +1
    for the zc map, to catch any  click and set it to 'from'
  */
    this.signalCatchFromMain = "+1"
  }
  
  catchTo(){
    /*
    This func is fired by search area component, 
    when it does, it sets the value of signalCatchTo to +1
    for the zc map, to catch any  click and set it to 'from'
  */
    this.signalCatchToMain = "+1"
  }

  userSelectedFrom(ev:any){
    /*
      This signal is fired  from zc map, it shall tell you  that zc map
      should no longer accept any click from user, as it  has already gotten  
      the response.
      Most importantly, it  sends this data to search area to show  it in the box,
      by setting 'msgSearchAreaFrom' to the chosen x,  y.
      ev: value of x, y  that user selected
    */
    this.valueFromParent = ev;
    this.signalCatchToMain = "-1"; // prevent zc map to cath any more clicks
    this.signalCatchFromMain = "-1"; // prevent zc map to cath any more clicks
    this.msgSearchAreaFrom = this.valueFromParent; // send data  to serachArea
  }

  userSelectedTo(ev:any){
    /*
      This signal is fired  from zc map, it shall tell you  that zc map
      should no longer accept any click from user, as it  has already gotten  
      the response.
      Most importantly, it  sends this data to search area to show  it in the box,
      by setting 'msgSearchAreaFrom' to the chosen x,  y.
      ev: value of x, y  that user selected
    */
    this.valueToParent = ev;
    this.signalCatchFromMain= "-1";
    this.signalCatchToMain = "-1";
    this.msgSearchAreaTo = this.valueToParent;
    
  }

  SearchApi(){
    /*
      It's fired   signal when user clicks   on search button
      fired by emitter  in   serach area called 'FinalSignal'
      it  just calls notify click  to send this final signal  to  zc-map 
      to call  the api from there.
    */
    this.notifyClick();
  }

  

  notifyClick() {
    /*
      It set varialbe that  is   being read by zc-map
      to send  them  as varialbles  when callin the API
    */
    this.FinalFromToZcMap =this.FinalFromParent ;
    this.FinalToToZcMap = this.FinalToParent;
    this.FinalAlgToZcMap = this.FinalAloParent;
    this.FinalCheckedToZcMap = this.FinalCheckedParent;
    //// by setting  next; it send   signal to zc-map to call API
    this.eventsSubject.next();
  }
}
