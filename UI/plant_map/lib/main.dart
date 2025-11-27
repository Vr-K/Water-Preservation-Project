import 'package:flutter/material.dart';
import 'dart:html' as html;
import 'dart:typed_data';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Plant App',
      theme: ThemeData(primarySwatch: Colors.green),
      debugShowCheckedModeBanner: false, // 👈 This hides the debug banner
      home: HomePage(),
      routes: {
        '/second': (context) => SecondPage(),
      },
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  Uint8List? _imageData;

  void _pickImage() {
    final input = html.FileUploadInputElement()..accept = 'image/*';
    input.click();

    input.onChange.listen((event) {
      final file = input.files?.first;
      if (file != null) {
        final reader = html.FileReader();
        reader.readAsArrayBuffer(file);
        reader.onLoadEnd.listen((event) {
          setState(() {
            _imageData = reader.result as Uint8List;
          });

          // Navigate to second page after image is picked
          Future.delayed(Duration(seconds: 1), () {
            Navigator.pushNamed(context, '/second');
          });
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Insert Image')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: _pickImage,
              child: Text('Insert Your Image'),
            ),
            SizedBox(height: 20),
            if (_imageData != null)
              Image.memory(_imageData!, width: 200, height: 200),
          ],
        ),
      ),
    );
  }
}

class SecondPage extends StatelessWidget {
  Widget _actionButton(String label) {
    return ElevatedButton(
      onPressed: () {
        // No action for now
      },
      child: Text(label),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Next Steps')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _actionButton('Plant Identification'),
            SizedBox(height: 16),
            _actionButton('View Heatmap'),
          ],
        ),
      ),
    );
  }
}
