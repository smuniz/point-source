; ModuleID = '../src/test52.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nounwind
define i32 @test52(i32 %param1, i32 %param2) #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %n = alloca i32, align 4
  %m = alloca i32, align 4
  store i32 %param1, i32* %1, align 4
  store i32 %param2, i32* %2, align 4
  %3 = load i32, i32* %1, align 4
  %4 = icmp eq i32 %3, 2
  br i1 %4, label %5, label %8

; <label>:5                                       ; preds = %0
  %6 = load i32, i32* %2, align 4
  %7 = add nsw i32 %6, 1
  store i32 %7, i32* %2, align 4
  br label %8

; <label>:8                                       ; preds = %5, %0
  store i32 0, i32* %n, align 4
  br label %9

; <label>:9                                       ; preds = %41, %8
  %10 = load i32, i32* %n, align 4
  %11 = icmp slt i32 %10, 10
  br i1 %11, label %12, label %44

; <label>:12                                      ; preds = %9
  %13 = load i32, i32* %2, align 4
  %14 = add nsw i32 %13, 10
  store i32 %14, i32* %2, align 4
  %15 = load i32, i32* %n, align 4
  %16 = icmp eq i32 %15, 5
  br i1 %16, label %17, label %20

; <label>:17                                      ; preds = %12
  %18 = load i32, i32* %1, align 4
  %19 = add nsw i32 %18, 2
  store i32 %19, i32* %1, align 4
  br label %20

; <label>:20                                      ; preds = %17, %12
  store i32 0, i32* %m, align 4
  br label %21

; <label>:21                                      ; preds = %27, %20
  %22 = load i32, i32* %m, align 4
  %23 = icmp slt i32 %22, 5
  br i1 %23, label %24, label %30

; <label>:24                                      ; preds = %21
  %25 = load i32, i32* %1, align 4
  %26 = add nsw i32 %25, 5
  store i32 %26, i32* %1, align 4
  br label %27

; <label>:27                                      ; preds = %24
  %28 = load i32, i32* %m, align 4
  %29 = add nsw i32 %28, 1
  store i32 %29, i32* %m, align 4
  br label %21

; <label>:30                                      ; preds = %21
  store i32 0, i32* %m, align 4
  br label %31

; <label>:31                                      ; preds = %37, %30
  %32 = load i32, i32* %m, align 4
  %33 = icmp slt i32 %32, 4
  br i1 %33, label %34, label %40

; <label>:34                                      ; preds = %31
  %35 = load i32, i32* %1, align 4
  %36 = add nsw i32 %35, 4
  store i32 %36, i32* %1, align 4
  br label %37

; <label>:37                                      ; preds = %34
  %38 = load i32, i32* %m, align 4
  %39 = add nsw i32 %38, 1
  store i32 %39, i32* %m, align 4
  br label %31

; <label>:40                                      ; preds = %31
  br label %41

; <label>:41                                      ; preds = %40
  %42 = load i32, i32* %n, align 4
  %43 = add nsw i32 %42, 1
  store i32 %43, i32* %n, align 4
  br label %9

; <label>:44                                      ; preds = %9
  %45 = load i32, i32* %1, align 4
  %46 = load i32, i32* %2, align 4
  %47 = add nsw i32 %45, %46
  ret i32 %47
}

attributes #0 = { nounwind "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "stack-protector-buffer-size"="8" "target-features"="+mmx,+sse,+sse2" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"clang version 3.8.0-2ubuntu4 (tags/RELEASE_380/final)"}
