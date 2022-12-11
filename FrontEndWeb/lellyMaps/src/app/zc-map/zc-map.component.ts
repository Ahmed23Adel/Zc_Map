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


  @Input() msgZcMapFromChild: any;
  @Input() msgZcMapToChild: any;
  @Output() valueFrom = new EventEmitter();
  @Output() valueTo = new EventEmitter();

  @Input() FinalFromParentZcMap: any;
  @Input() FinalToParentZcMap: any;
  @Input() FinalAlgoParentZcMap: any;
  @Input() FinalCheckedParentZcMap: any;
  @Input('clickSubject') clickSubject:any;

  
  // @Input('clickSubject') clickSubject:any;


  zc_map: string[] [];
  isSelectFrom = false;
  isSelectTo = false;
  selectFrom = -1;
  selectTo = -1;
  
  constructor(private zcMap: ZcMapServiceService, private solServiceData:SolutionBackedService){
    this.zc_map = zcMap.getMap()
    console.log(this.zc_map)
  }
  private eventsSubscription: Subscription;

  @Input() events: Observable<void>;
  
  ngOnInit(){
    this.eventsSubscription = this.events.subscribe(() => this.SearchApi());
  }
  
  ngOnDestroy() {
    this.eventsSubscription.unsubscribe();
  }



  select(indexRow:number, indexCol:number){
    if(this.msgZcMapFromChild == "+1"){
      // console.log("User selected" , indexRow, indexCol);
      this.valueFrom.emit(indexRow+","+indexCol);
    }
    // console.log("select",this.msgZcMapToChild)
    if(this.msgZcMapToChild == "+1"){
      // console.log("User selected" , indexRow, indexCol);
      this.valueTo.emit(indexRow+","+indexCol);
    }

    
    
  }

  selctFrom(ev:any){
    console.log("yousef")
  }

  SearchApi(){
    console.log("SearchChildZcMap", this.FinalAlgoParentZcMap)
    console.log("SearchChildZcMap", this.FinalFromParentZcMap)
    console.log("SearchChildZcMap", this.FinalToParentZcMap)
    console.log("SearchChildZcMap", this.FinalCheckedParentZcMap)
    for(let i =0; i<81; i++){
      for (let j=0; j<78; j++){
        let current_id = "cell-"+i+"-"+j; // here you have that id
        // console.log(current_id);
          let crnt_cell = document.getElementById(current_id)as HTMLInputElement;
          crnt_cell.style.borderRadius = "0px";
          crnt_cell.style.borderWidth = "0px";
      }
    }

    this.solServiceData.getSolution(this.FinalFromParentZcMap, this.FinalToParentZcMap,this.FinalAlgoParentZcMap ).subscribe(
      serviceData=>{
        console.log("serviceData in zc map");
        console.log(serviceData.alg_output)
        for(let i=0; i<serviceData.alg_output.length; i++){
          let current_id = serviceData.alg_output[i]; // here you have that id
          let crnt_cell = document.getElementById(current_id)as HTMLInputElement;
          //box-sizing: border-box;
          // border-radius: 5px;
          // border-color: greenyellow;
          // border-style: solid;
          // console.log(current_id, crnt_cell)
          console.log(current_id, crnt_cell)
          crnt_cell.style.borderRadius = "50px";
          crnt_cell.style.borderWidth = "5px";
          crnt_cell.style.borderColor = "blue";
          crnt_cell.style.borderStyle = "solid";
          // crnt_cell.style.borderStyle = "solid";
          
        }
      }
    )
  }

  SearchSubmit(){
    console.log("SearchSubmitSearchSubmitSearchSubmit")
  }

}
