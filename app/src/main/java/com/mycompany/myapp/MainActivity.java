package com.mycompany.myapp;

import android.content.*;
import android.database.*;
import android.database.sqlite.*;
import android.os.*;
import android.support.v7.app.*;
import android.view.*;
import android.widget.*;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ListView listView=(ListView) findViewById(R.id.list);
        listView.setOnItemClickListener(itemClickListener);
    }
AdapterView.OnItemClickListener itemClickListener=new AdapterView.OnItemClickListener() {
    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        if(i==0){
            Intent intent =new Intent(MainActivity.this,Otsosuki.class);
startActivity(intent);
      
	
	}
    }
	
};

	
	
}
