import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CountryService {

  constructor(private http: HttpClient) {
  }

  getCountry() {
    return this.http.get <any>('/api/country/options');
  }

}
