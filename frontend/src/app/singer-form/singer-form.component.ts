import { Component, OnInit } from '@angular/core';
import {FormBuilder, Validators} from '@angular/forms';
import {SingerService} from '../service/singer.service';
import {ActivatedRoute, Router} from '@angular/router';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-singer-form',
  templateUrl: './singer-form.component.html',
  styleUrls: ['./singer-form.component.scss']
})
export class SingerFormComponent implements OnInit {

  singerFormGroup;

  constructor(private fb: FormBuilder, public singerService: SingerService, private router: Router, private route: ActivatedRoute,
              private http: HttpClient) { }

  ngOnInit() {
    this.singerFormGroup = this.fb.group({
      id: [null],
      alias: [null],
      first_name: [null, Validators.required],
      last_name: [null, Validators.required],
      year_of_birth: [null, Validators.min(1600)],
      active: [true],
    });

    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.http.get('/api/person/' + id + '/get').subscribe((response) => {
        this.singerFormGroup.patchValue(response);
      });
    }
  }

  createSinger() {
    const singer = this.singerFormGroup.value;
    if (singer.id) {
      this.singerService.updateSinger(singer).
      subscribe((response: any[]) => {
        this.router.navigate(['/singer-list/']);
      });
    } else {
      this.singerService.createSinger(singer).
      subscribe(() => {
        this.router.navigate(['/singer-list/']);
      });
    }
  }

}
