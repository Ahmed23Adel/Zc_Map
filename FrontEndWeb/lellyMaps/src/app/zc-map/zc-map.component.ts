import { Component, EventEmitter, Input, Output } from '@angular/core';
import { ZcMapServiceService } from 'src/zc-map-service.service';

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
  zc_map: string[] [];
  isSelectFrom = false;
  isSelectTo = false;
  selectFrom = -1;
  selectTo = -1;
  
  constructor(private zcMap: ZcMapServiceService){
    this.zc_map = zcMap.getMap()
    console.log(this.zc_map)
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


}
