# uiautomation-runner

> 标签: JavaScript

## 简介

require('uiautomation-runner').build_and_test {       build_dir:            "#{__dirname}/build/xcode"       results_dir:          "#{__dirname}/results/#{strftime.strftimeUTC('...')}"       script_path:          "#{__dirname}/all-the-tests.js"       xcode_workspace:      "#{__dirname}/../MyAwesomeProduct.xcworkspace"       xcode_scheme:         'myawesomeproduct'       xcode_configuration:  'Test'       app_filename:         'My Awesome Product.app'       delete_simulator_apps: true     }

## 官网

- npm 页面：https://www.npmjs.com/package/uiautomation-runner

## 历史版本号

- 当前版本：0.0.4

- 0.0.1
- 0.0.2
- 0.0.3
- 0.0.4

## 获取地址

- npm 安装：`npm install uiautomation-runner`
- npm registry：https://registry.npmjs.org/uiautomation-runner
- Node 要求：>=0.8.0
