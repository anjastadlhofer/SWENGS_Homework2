import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {FormBuilder, Validators} from '@angular/forms';
import {ActivatedRoute, Router} from '@angular/router';
import {GenreService} from '../service/genre.service';
import {SongService} from '../service/song.service';
import {CountryService} from '../service/country.service';

@Component({
  selector: 'app-song-form',
  templateUrl: './song-form.component.html',
  styleUrls: ['./song-form.component.scss']
})
export class SongFormComponent implements OnInit {

  songFormGroup;
  countryOptions;
  personOptions;

  constructor(private fb: FormBuilder, private http: HttpClient, private route: ActivatedRoute, private router: Router,
              public genreService: GenreService, public songService: SongService, public countryService: CountryService) { }

  ngOnInit() {
    this.songFormGroup = this.fb.group({
      id: [null],
      title: ['', Validators.required],
      genre: [null],
      release_date: [null, Validators.required],
      story: ['', Validators.required],
      selled: [0],
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
        this.countryOptions = result; });
  }

  createSong() {
    const song = this.songFormGroup.value;
    if (song.id) {
      this.songService.updateSong(song).
      subscribe((response: any[]) => {
        alert('updated successfully');
      });
    } else {
      this.songService.createSong(song).
      subscribe(() => {
        this.router.navigate(['/song-list/']);
      });
    }
  }

}
