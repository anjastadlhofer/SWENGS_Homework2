import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SingerFormComponent } from './singer-form.component';

describe('SingerFormComponent', () => {
  let component: SingerFormComponent;
  let fixture: ComponentFixture<SingerFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SingerFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SingerFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
