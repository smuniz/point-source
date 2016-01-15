; ModuleID = '../src/test15.c'
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.simple = type { i32, i32 }

@fred = internal global [2 x %struct.simple] [%struct.simple { i32 1, i32 2 }, %struct.simple { i32 3, i32 4 }], align 16

; Function Attrs: nounwind
define i32 @test15(i32 %value1) #0 {
  %1 = alloca i32, align 4
  %local = alloca i32, align 4
  %n = alloca i32, align 4
  store i32 %value1, i32* %1, align 4
  store i32 0, i32* %n, align 4
  br label %2

; <label>:2                                       ; preds = %18, %0
  %3 = load i32* %n, align 4
  %4 = icmp slt i32 %3, 2
  br i1 %4, label %5, label %21

; <label>:5                                       ; preds = %2
  %6 = load i32* %n, align 4
  %7 = sext i32 %6 to i64
  %8 = getelementptr inbounds [2 x %struct.simple]* @fred, i32 0, i64 %7
  %9 = getelementptr inbounds %struct.simple* %8, i32 0, i32 0
  %10 = load i32* %9, align 4
  store i32 %10, i32* %local, align 4
  %11 = load i32* %n, align 4
  %12 = sext i32 %11 to i64
  %13 = getelementptr inbounds [2 x %struct.simple]* @fred, i32 0, i64 %12
  %14 = getelementptr inbounds %struct.simple* %13, i32 0, i32 1
  %15 = load i32* %14, align 4
  %16 = load i32* %local, align 4
  %17 = add nsw i32 %16, %15
  store i32 %17, i32* %local, align 4
  br label %18

; <label>:18                                      ; preds = %5
  %19 = load i32* %n, align 4
  %20 = add nsw i32 %19, 1
  store i32 %20, i32* %n, align 4
  br label %2

; <label>:21                                      ; preds = %2
  %22 = load i32* %local, align 4
  ret i32 %22
}

attributes #0 = { nounwind "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-realign-stack" "stack-protector-buffer-size"="8" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.ident = !{!0}

!0 = !{!"Ubuntu clang version 3.6.2-1 (tags/RELEASE_362/final) (based on LLVM 3.6.2)"}
