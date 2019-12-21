import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class GenreService {

  constructor() {
  }

  genreNames = {
    r: 'Rock',
    p: 'Pop',
    j: 'Jazz',
    h: 'Hip Hop',
    m: 'Metal'
  };

}
