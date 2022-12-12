import { Component, EventEmitter, Input, Output } from '@angular/core';
import { ZcMapServiceService } from 'src/zc-map-service.service';
import { SolutionBackedService } from '../solution-backed.service';
import { Observable, Subject, Subscription } from 'rxjs';

@Component({
  selector: 'app-zc-map',
  templateUrl: './zc-map.component.html',
  styleUrls: ['./zc-map.component.scss']
})
export class ZcMapComponent {

  ////////////////////////////////
  //////// If it equal to +1, it will catch click on images
  @Input() signalZcMapFromChild: any;
  @Input() signalZcMapToChild: any;
  ////////////////////////////////
  //////////////////////////////
  ////// Emit the value of x, and y that used clicked on
  @Output() valueFrom = new EventEmitter();
  @Output() valueTo = new EventEmitter();
  //////////////////////////////
  /////////////////////////////
  /////// Final values to zc map to send them to api
  @Input() FinalFromParentZcMap: any;
  @Input() FinalToParentZcMap: any;
  @Input() FinalAlgoParentZcMap: any;
  @Input() FinalCheckedParentZcMap: any;
  @Input('clickSubject') clickSubject:any; // signal to fire API
  /////////////////////////////

  /////////////////////////////
  ///////To fire the api signal
  private eventsSubscription: Subscription;
  @Input() events: Observable<void>;
  /////////////////////////////


  zc_map: string[] []; // zc map to display as images
  isSelectFrom = false;
  isSelectTo = false;
  selectFrom = -1;
  selectTo = -1;
  
  constructor(private zcMap: ZcMapServiceService, private solServiceData:SolutionBackedService){
    /**
     * use solServiceData to call the api
     * zcMap to get the map
     */
    this.zc_map = zcMap.getMap()
  }
  
  
  ngOnInit(){
    /**
     * subscirbe to the event; to call API when parent sends such signal
     * this signal will be based on clicking on search button in search aread
     */
    this.eventsSubscription = this.events.subscribe(() => this.SearchApi());
  }
  
  ngOnDestroy() {
    /**
     * unsubscribe from even
     */
    this.eventsSubscription.unsubscribe();
  }



  select(indexRow:number, indexCol:number){
    /**
     * is fired only when user click on any image
     * but it doesn't emit the value clicked on unless 
     * main component sent a signal speicified by
     *  signalZcMapFromChild, and signalZcMapToChild
     */
    if(this.signalZcMapFromChild == "+1"){
      this.valueFrom.emit(indexRow+","+indexCol);
    }
    if(this.signalZcMapToChild == "+1"){
      this.valueTo.emit(indexRow+","+indexCol);
    }
  }

  SearchApi(){
    console.log("SearchChildZcMap", this.FinalAlgoParentZcMap)
    console.log("SearchChildZcMap", this.FinalFromParentZcMap)
    console.log("SearchChildZcMap", this.FinalToParentZcMap)
    console.log("SearchChildZcMap", this.FinalCheckedParentZcMap)
    /**
     * Cleaning the map first from any previous drawings
     */
    for(let i =0; i<81; i++){
      for (let j=0; j<78; j++){
        let current_id = "cell-"+i+"-"+j; // here you have that id
        // console.log(current_id);
          let crnt_cell = document.getElementById(current_id)as HTMLInputElement;
          crnt_cell.style.borderRadius = "0px";
          crnt_cell.style.borderWidth = "0px";
      }
    }
    /**
     * draw the  new solutoin
     */
    this.solServiceData.getSolution(this.FinalFromParentZcMap, this.FinalToParentZcMap,this.FinalAlgoParentZcMap ).subscribe(
      serviceData=>{
        console.log("serviceData in zc map");
        console.log(serviceData.alg_output)
        for(let i=0; i<serviceData.alg_output.length; i++){
          // draw blue circle on each cell chosen
          let current_id = serviceData.alg_output[i]; // here you have that id
          let crnt_cell = document.getElementById(current_id)as HTMLInputElement;
          crnt_cell.style.borderRadius = "50px";
          crnt_cell.style.borderWidth = "5px";
          crnt_cell.style.borderColor = "blue";
          crnt_cell.style.borderStyle = "solid";
          
        }
      }
    )
  }

}
