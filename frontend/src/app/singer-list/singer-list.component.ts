import { Component, OnInit } from '@angular/core';
import {SingerService} from '../service/singer.service';

@Component({
  selector: 'app-singer-list',
  templateUrl: './singer-list.component.html',
  styleUrls: ['./singer-list.component.scss']
})
export class SingerListComponent implements OnInit {

  singers: any[];
  displayedColumns = ['alias', 'first_name', 'last_name', 'year_of_birth', 'active', 'id'];

  constructor(public singerService: SingerService) { }

  ngOnInit() {
    this.singerService.getSingers()
      .subscribe((response: any[]) => {
        this.singers = response;
      });
  }

  deleteSinger(singers) {
    this.singerService.deleteSinger(singers.id).
    subscribe((response: any[]) => {
      this.ngOnInit();
    });
  }

}
