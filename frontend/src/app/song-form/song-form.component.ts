import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {AbstractControl, FormBuilder, ValidatorFn, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {GenreService} from '../service/genre.service';
import {SongService} from '../service/song.service';
import {CountryService} from '../service/country.service';
import {SingerService} from '../service/singer.service';

@Component({
  selector: 'app-song-form',
  templateUrl: './song-form.component.html',
  styleUrls: ['./song-form.component.scss']
})
export class SongFormComponent implements OnInit {

  songFormGroup;
  countryOptions;
  singerOptions;

  constructor(private fb: FormBuilder, private http: HttpClient, private route: ActivatedRoute, private router: Router,
              public genreService: GenreService, public songService: SongService, public countryService: CountryService,
              public singerService: SingerService) { }

  ngOnInit() {
    this.songFormGroup = this.fb.group({
      id: [null],
      title: ['', [Validators.required, this.WordValidator()]],
      genre: [null, Validators.required],
      release_date: [null, Validators.required],
      story: ['', Validators.required],
      selled: [0, Validators.min(1)],
      band: [true],
      country: [null],
      singers: [[]],
    });

    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.http.get('/api/song/' + id + '/get').subscribe((response) => {
        this.songFormGroup.patchValue(response);
      });
    }

    this.countryService.getCountry()
      .subscribe((result) => {
        this.countryOptions = result;
      });

    this.singerService.getSingers()
      .subscribe((result) => {
        this.singerOptions = result;
      });
  }

  createSong() {
    const song = this.songFormGroup.value;
    if (song.id) {
      this.songService.updateSong(song).
      subscribe((response: any[]) => {
        this.router.navigate(['/song-list/']);
      });
    } else {
      this.songService.createSong(song).
      subscribe(() => {
        this.router.navigate(['/song-list/']);
      });
    }
  }

  WordValidator(): ValidatorFn {
    return (control: AbstractControl): {[key: string]: any} | null => {
      const forbidden = /fuck/.test(control.value);
      return forbidden ? {fuck: {value: control.value}} : null;
    };
  }

}
